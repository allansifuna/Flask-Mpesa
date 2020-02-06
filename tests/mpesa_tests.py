from flask import Flask
from flask_mpesa import MpesaAPI
import click

app=Flask(__name__)

app.config["API_ENVIRONMENT"] = "sandbox"
app.config["APP_KEY"] = "vbxsneeZ9IMFoyKKIgOIQQZFlawAADnP"
app.config["APP_SECRET"] = "WAzDhQVhitIXwiTc"
mp = MpesaAPI(app)


@click.command()
def test():
    """Run the tests."""
    import pytest
    rv = pytest.main([TEST_PATH, '--verbose'])
    exit(rv)
