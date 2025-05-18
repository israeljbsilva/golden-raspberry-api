import logging
from pathlib import Path

from sqlmodel import Session, SQLModel, create_engine, select

from app.csv_reader import MovieCsv
from app.models import Movie
from app.services import load_csv_to_db

logger = logging.getLogger(__name__)


BASE_DIR = Path(__file__).resolve().parent.parent
CSV_FILE_PATH = BASE_DIR / "app" / "data" / "movielist.csv"
DATABASE_URL = "sqlite:///:memory:"
engine = create_engine(DATABASE_URL, echo=False)


def init_db():
    SQLModel.metadata.create_all(engine)


def get_session():
    movies = MovieCsv.read_csv_file(file_path=CSV_FILE_PATH)

    with Session(engine) as session:
        try:
            init_db()
            existing_movie = session.exec(select(Movie).limit(1)).first()
            if not existing_movie:
                load_csv_to_db(movies, session)
            yield session
        except Exception as e:
            logger.error(f"Error initializing session {str(e)}")
            raise
