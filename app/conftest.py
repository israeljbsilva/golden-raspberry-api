import pytest
from sqlmodel import Session, SQLModel

from app.csv_reader import MovieCsv
from app.database import engine, get_session
from app.main import app
from app.services import load_csv_to_db


@pytest.fixture
def override_get_session_single_producer():
    def mock_session():
        with Session(engine) as new_session:
            SQLModel.metadata.create_all(engine)
            load_test_data_single_producer(new_session)
            yield new_session

    app.dependency_overrides[get_session] = mock_session  # noqa
    yield
    app.dependency_overrides.clear()  # noqa


@pytest.fixture
def override_get_session_comma_separated():
    def mock_session():
        with Session(engine) as new_session:
            SQLModel.metadata.create_all(engine)
            load_test_data_comma_separated(new_session)
            yield new_session

    app.dependency_overrides[get_session] = mock_session  # noqa
    yield
    app.dependency_overrides.clear()  # noqa


@pytest.fixture
def override_get_session_comma_and():
    def mock_session():
        with Session(engine) as new_session:
            SQLModel.metadata.create_all(engine)
            load_test_data_comma_and(new_session)
            yield new_session

    app.dependency_overrides[get_session] = mock_session  # noqa
    yield
    app.dependency_overrides.clear()  # noqa


def load_test_data_single_producer(session: Session):
    movies = [
        MovieCsv(year=1985, title="Movie E", studios="Studio E", producers="Producer A", winner=True),
        MovieCsv(year=1986, title="Movie F", studios="Studio F", producers="Producer B", winner=True),
        MovieCsv(year=1987, title="Movie K", studios="Studio K", producers="Producer C", winner=True),
        MovieCsv(year=1988, title="Movie L", studios="Studio L", producers="Producer D", winner=True),
        MovieCsv(year=1989, title="Movie M", studios="Studio M", producers="Producer X", winner=True),
        MovieCsv(year=1990, title="Movie A", studios="Studio A", producers="Joel Silver", winner=True),
        MovieCsv(year=1991, title="Movie B", studios="Studio B", producers="Joel Silver", winner=True),
        MovieCsv(year=2000, title="Movie C", studios="Studio C", producers="Matthew Vaughn", winner=True),
        MovieCsv(year=2005, title="Movie G", studios="Studio G", producers="Producer Z", winner=True),
        MovieCsv(year=2010, title="Movie H", studios="Studio H", producers="Producer W", winner=True),
        MovieCsv(year=1993, title="Movie I", studios="Studio I", producers="Producer V", winner=True),
        MovieCsv(year=2015, title="Movie J", studios="Studio J", producers="Producer U", winner=True),
        MovieCsv(year=2013, title="Movie D", studios="Studio D", producers="Matthew Vaughn", winner=True),
    ]
    load_csv_to_db(movies, session)
    return movies


def load_test_data_comma_separated(session: Session):
    movies = [
        MovieCsv(year=1992, title="Movie A", studios="Studio A", producers="Anna Smith, Producer X", winner=True),
        MovieCsv(year=1993, title="Movie E", studios="Studio E", producers="Producer A, Producer B", winner=True),
        MovieCsv(year=1994, title="Movie F", studios="Studio F", producers="Producer C, Producer D", winner=True),
        MovieCsv(year=2007, title="Movie G", studios="Studio G", producers="Producer E, Producer F", winner=True),
        MovieCsv(year=1995, title="Movie B", studios="Studio B", producers="Producer Y, Anna Smith", winner=True),
        MovieCsv(year=2003, title="Movie C", studios="Studio C", producers="Bob Jones, Producer Z", winner=True),
        MovieCsv(year=2011, title="Movie H", studios="Studio H", producers="Producer G, Producer H", winner=True),
        MovieCsv(year=2013, title="Movie D", studios="Studio D", producers="Bob Jones, Producer W", winner=True),
        MovieCsv(year=1990, title="Movie I", studios="Studio I", producers="Producer I, Producer J", winner=True),
        MovieCsv(year=2014, title="Movie J", studios="Studio J", producers="Producer K, Producer L", winner=True),
    ]
    load_csv_to_db(movies, session)
    return movies


def load_test_data_comma_and(session: Session):
    movies = [
        MovieCsv(year=1994, title="Movie A", studios="Studio A", producers="Clara Lee, Producer X and Producer Y", winner=True),
        MovieCsv(year=1996, title="Movie F", studios="Studio F", producers="Producer C, Producer D and Producer E", winner=True),
        MovieCsv(year=1999, title="Movie B", studios="Studio B", producers="David Brown, Producer Z and Clara Lee", winner=True),
        MovieCsv(year=1986, title="Movie C", studios="Studio C", producers="Producer W and Producer V", winner=True),
        MovieCsv(year=1989, title="Movie E", studios="Studio E", producers="Producer A and Producer B", winner=True),
        MovieCsv(year=2001, title="Movie G", studios="Studio G", producers="Producer F and Producer G", winner=True),
        MovieCsv(year=2008, title="Movie H", studios="Studio H", producers="Producer H, Producer I and Producer J", winner=True),
        MovieCsv(year=2010, title="Movie D", studios="Studio D", producers="David Brown and Producer U", winner=True),
        MovieCsv(year=2012, title="Movie I", studios="Studio I", producers="Producer K and Producer L", winner=True),
        MovieCsv(year=2016, title="Movie J", studios="Studio J", producers="Producer M, Producer N and Producer O", winner=True),
    ]
    load_csv_to_db(movies, session)
    return movies
