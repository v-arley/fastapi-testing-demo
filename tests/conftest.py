import pytest
from fastapi.testclient import TestClient

from app.main import app, get_db
from app.database import Database


@pytest.fixture
def fake_db():
    return Database()


@pytest.fixture
def client(fake_db):
    app.dependency_overrides[get_db] = lambda: fake_db

    with TestClient(app) as test_client:
        yield test_client

    app.dependency_overrides.clear()