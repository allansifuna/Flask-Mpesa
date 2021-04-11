import pytest
from .base import mp, app


@pytest.mark.usefixtures("environment")
def test_environment(environment):
    """
    Test the required environment .
    """
    test_environment = app.config.get("API_ENVIRONMENT")
    assert test_environment == environment


@pytest.mark.usefixtures("credentials")
def test_get_credentials(credentials):
    """ Test to assert that the credentials are correctly read to the app.config dict"""
    test_creds = mp.get_credentials()
    assert test_creds == credentials
