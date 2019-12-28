# Flask-Mpesa

Flask-Mpesa is a mpesa-py extension for flask Applications.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install flask-mpesa.

```bash
pip install flask-mpesa
```

## Usage

```python
from flask import Flask
from flask_mpesa import MpesaAPI

app=Flask(__name__)


mpesaapi=MpesaAPI(app)
```


## if you are using blueprints
```python
from flask_mpesa import MpesaAPI
mpesaapi=MpesaAPI()

mpesaapi.init_app(app)
```
### Be sure to set the following variables in the app.config 

```python
app.config["API_ENVIRONMENT"] = "sandbox" #sandbox or live
app.config["APP_KEY"] = "..." # App_key from developers portal
app.config["APP_SECRET"] = "..." #App_Secret from developers portal
``` 
### B2C  Api

```python
b2c=mpesaapi.B2C 

```
### B2B  Api

```python

b2b=mpesaapi.B2B

```

### C2B  api

```python
c2b=mpesaapi.C2B

```

### MpesaExpress  api

```python
data = {
        "business_shortcode": , #from developers portal
        "passcode": " ",#from developers portal
        "amount": 1, # choose amount preferrably KSH 1
        "phone_number": "", #phone number to be prompted to pay
        "callback_url": "http://0.0.0.0:5000/buy", # cllback url should be exposes. for testing putposes you can route on host 0.0.0.0 and set the callback url to be https://youripaddress:yourport/endpoint
        "description": "first test" #a description of the transaction its optional
    }
    v = mp.MpesaExpress.stk_push(**data)  # ** unpacks the dictionary

```
### Balance  api

```python
balance=mpesaapi.Balance

```
### Reversal  api

```python
reversal=mpesaapi.Reversal

```
### TransactionStatus  api

```python
transaction_status=mpesaapi.TransactionStatus

```
## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
## Tests and Examples

Examples are comming soon!.
## License
[MIT](https://choosealicense.com/licenses/mit/)
