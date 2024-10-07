import pytest

from server import app

@pytest.fixture
def client():
    client = app.test_client()
    yield client


def test_landing(client):
    response = client.get("/health")
    assert b"OK" in response.data
