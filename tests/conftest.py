from falcon import testing
import pytest

from timing.app import app


@pytest.fixture
def client():
    return testing.TestClient(app)
