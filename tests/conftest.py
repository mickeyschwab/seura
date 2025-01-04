import pytest
from seura import SeuraClient


@pytest.fixture
def client():
    return SeuraClient(host="127.0.0.1")
