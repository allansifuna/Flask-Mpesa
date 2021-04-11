import pytest
import  os

def client_credentials(*args,**kwargs):
    def wrapper(func):



@pytest.fixture(name="environment")
def fixture_environment():
    return "sandbox"

@pytest.fixture(name="credentials")
def fixture_get_credentials():
    return "sandbox",os.environ.get("MPESA_API_KEY"),os.environ.get("MPESA_API_SECRET")

@pytest.fixture(name="b2b")
def fixture_mock_b2b():
    return "sandbox"
