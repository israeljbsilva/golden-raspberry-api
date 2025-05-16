from fastapi import FastAPI
from contextlib import asynccontextmanager

from app.csv_reader import MovieCsv


@asynccontextmanager
async def lifespan(app: FastAPI):
    movies = MovieCsv.read_csv_file(file_path="app/data/movielist.csv")

    yield

app = FastAPI(title="Golden Raspberry Awards API", lifespan=lifespan)
