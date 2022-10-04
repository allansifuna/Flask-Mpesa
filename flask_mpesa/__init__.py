from flask import Blueprint, current_app
import warnings
from flask_mpesa.api.b2c import MpesaBase
from flask_mpesa.api.b2c import B2C
from flask_mpesa.api.c2b import C2B
from flask_mpesa.api.b2b import B2B
from flask_mpesa.api.balance import Balance
from flask_mpesa.api.mpesa_express import MpesaExpress
from flask_mpesa.api.reversal import Reversal
from flask_mpesa.api.transaction_status import TransactionStatus


class MpesaAPI(object):

    def __init__(self, app=None, **kwargs):
        self.app = app
        self.sandbox_url = "https://sandbox.safaricom.co.ke"
        self.live_url = "https://api.safaricom.co.ke"

        if app:
            self.init_app(app)

    def init_app(self, app):
        if('APP_KEY' not in app.config and 'APP_SECRET' not in app.config and 'API_ENVIRONMENT' not in app.config):
            warnings.warn(
                'Neither APP_KEY nor APP_SECRET nor API_ENVIRONMENT is set')

        self.app = app
        self.register_blueprint(app)

    @staticmethod
    def register_blueprint(app):
        module = Blueprint('mpesaapi', __name__, template_folder='templates')
        app.register_blueprint(module)
        return module

    def get_credentials(self):
        """Helper method to return app_key, app_secret and api_environmentfrom the app's config."""
        api_env = self.app.config.get("API_ENVIRONMENT")
        app_key = self.app.config.get("APP_KEY")
        app_secret = self.app.config.get("APP_SECRET")
        return api_env, app_key, app_secret

    def get_app(self, reference_app=None):
        """Helper method that implements the logic to look up an
        application."""

        if reference_app is not None:
            return reference_app

        if current_app:
            return current_app._get_current_object()

        if self.app is not None:
            return self.app

        raise RuntimeError(
            'No application found. Either work inside a view function or push'
            ' an application context.'
        )

    @property
    def C2B(self):
        """Method returns a C2B Object"""
        env, app_key, app_secret = self.get_credentials()
        return C2B(env, app_key, app_secret, self.sandbox_url, self.live_url)

    @property
    def B2C(self):
        """Method returns a B2C Object"""
        env, app_key, app_secret = self.get_credentials()
        return B2C(env, app_key, app_secret, self.sandbox_url, self.live_url)

    @property
    def B2B(self):
        """Method returns a B2B Object"""
        env, app_key, app_secret = self.get_credentials()
        return B2B(env, app_key, app_secret, self.sandbox_url, self.live_url)

    @property
    def Balance(self):
        """Method returns a Balance Object"""
        env, app_key, app_secret = self.get_credentials()
        return Balance(env, app_key, app_secret, self.sandbox_url, self.live_url)

    @property
    def MpesaExpress(self):
        """Method returns a MpesaExpress Object"""
        env, app_key, app_secret = self.get_credentials()
        return MpesaExpress(env, app_key, app_secret, self.sandbox_url, self.live_url)

    @property
    def Reversal(self):
        """Method returns a Reversal Object"""
        env, app_key, app_secret = self.get_credentials()
        return Reversal(env, app_key, app_secret, self.sandbox_url, self.live_url)

    @property
    def TransactionStatus(self):
        """Method returns a TransactionSatus Object"""
        env, app_key, app_secret = self.get_credentials()
        return TransactionStatus(env, app_key, app_secret, self.sandbox_url, self.live_url)
