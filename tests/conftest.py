import pytest
from falcon import testing

from timing.app import app


@pytest.fixture
def client():
    return testing.TestClient(app)
