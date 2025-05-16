from fastapi import FastAPI
from contextlib import asynccontextmanager

from sqlmodel import Session

from app.csv_reader import MovieCsv
from app.database import engine, init_db
from app.services import load_csv_to_db


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()

    movies = MovieCsv.read_csv_file(file_path="app/data/movielist.csv")

    with Session(engine) as session:
        load_csv_to_db(movies, session)

    yield

app = FastAPI(title="Golden Raspberry Awards API", lifespan=lifespan)
