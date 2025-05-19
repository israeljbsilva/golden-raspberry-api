from fastapi.testclient import TestClient

from app.csv_reader import MovieCsv
from app.main import app
from app.services import load_csv_to_db

client = TestClient(app)


def load_test_data(session):
    movies = [
        MovieCsv(year=1980, title="Movie A", studios="Studio A", producers="Producer A", winner=True),
        MovieCsv(year=1985, title="Movie B", studios="Studio B", producers="Producer A", winner=True),
        MovieCsv(year=1990, title="Movie C", studios="Studio C", producers="Producer B", winner=True),
        MovieCsv(year=1991, title="Movie D", studios="Studio D", producers="Producer B", winner=True)
    ]
    load_csv_to_db(movies, session)
    return movies


def test_get_producer_intervals(override_get_session):
    response = client.get("/producers/intervals")
    assert response.status_code == 200
    data = response.json()

    expected = {
        "min": [
            {
                "producer": "Producer B",
                "interval": 1,
                "previousWin": 1990,
                "followingWin": 1991
            }
        ],
        "max": [
            {
                "producer": "Producer A",
                "interval": 5,
                "previousWin": 1980,
                "followingWin": 1985
            }
        ]
    }
    assert data == expected


def test_get_movies(override_get_session):
    response = client.get("/movies")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 4
    assert data[0]["title"] == "Movie A"
    assert data[1]["title"] == "Movie B"
    assert data[2]["title"] == "Movie C"
    assert data[3]["title"] == "Movie D"
