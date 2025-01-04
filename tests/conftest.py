import pytest
from seura import SeuraClient


@pytest.fixture
def client():
    return SeuraClient(ip_address="127.0.0.1")
