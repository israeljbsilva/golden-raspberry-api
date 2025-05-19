import pytest
from sqlmodel import Session, SQLModel

from app.database import engine, get_session
from app.main import app
from app.tests.test_api import load_test_data


@pytest.fixture
def override_get_session():
    def mock_session():
        with Session(engine) as new_session:
            SQLModel.metadata.create_all(engine)
            load_test_data(new_session)
            yield new_session

    app.dependency_overrides[get_session] = mock_session  # noqa
    yield
    app.dependency_overrides.clear()  # noqa
