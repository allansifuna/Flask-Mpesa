from flask import Flask
from flask_mpesa import MpesaAPI
import os
app = Flask(__name__)

app.config["API_ENVIRONMENT"] = "sandbox"
app.config["APP_KEY"] = os.environ.get("MPESA_API_KEY")
app.config["APP_SECRET"] = os.environ.get("MPESA_API_SECRET")
mp = MpesaAPI(app)
