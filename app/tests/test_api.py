from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_get_producer_intervals_single_producer(override_get_session_single_producer):
    response = client.get("/producers/intervals")
    assert response.status_code == 200
    data = response.json()

    expected = {
        "min": [
            {
                "producer": "Joel Silver",
                "interval": 1,
                "previousWin": 1990,
                "followingWin": 1991
            }
        ],
        "max": [
            {
                "producer": "Matthew Vaughn",
                "interval": 13,
                "previousWin": 2000,
                "followingWin": 2013
            }
        ]
    }
    assert data == expected


def test_get_producer_intervals_comma_separated(override_get_session_comma_separated):
    response = client.get("/producers/intervals")
    assert response.status_code == 200
    data = response.json()

    expected = {
        "min": [
            {
                "producer": "Anna Smith",
                "interval": 3,
                "previousWin": 1992,
                "followingWin": 1995
            }
        ],
        "max": [
            {
                "producer": "Bob Jones",
                "interval": 10,
                "previousWin": 2003,
                "followingWin": 2013
            }
        ]
    }
    assert data == expected


def test_get_producer_intervals_comma_and(override_get_session_comma_and):
    response = client.get("/producers/intervals")
    assert response.status_code == 200
    data = response.json()

    expected = {
        "min": [
            {
                "producer": "Clara Lee",
                "interval": 5,
                "previousWin": 1994,
                "followingWin": 1999
            }
        ],
        "max": [
            {
                "producer": "David Brown",
                "interval": 11,
                "previousWin": 1999,
                "followingWin": 2010
            }
        ]
    }
    assert data == expected
