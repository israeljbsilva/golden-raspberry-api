from sqlmodel import Session

from app.csv_reader import MovieCsv
from app.models import Movie


def load_csv_to_db(movies: list[MovieCsv], session: Session):
    for movie_csv in movies:
        movie_model = Movie(
            year=movie_csv.year,
            title=movie_csv.title,
            studios=movie_csv.studios,
            producers=movie_csv.producers,
            winner=movie_csv.winner
        )

        session.add(movie_model)

    session.commit()
