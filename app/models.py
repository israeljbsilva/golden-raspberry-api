from sqlmodel import Field, SQLModel


class Movie(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    year: int
    title: str
    studios: str
    producers: str
    winner: bool
