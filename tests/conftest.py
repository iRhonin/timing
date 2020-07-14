import pytest
from falcon import testing

from timing.app import create_app


@pytest.fixture
def client():
    app = create_app()
    return testing.TestClient(app)
