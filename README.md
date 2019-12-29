# Flask-Mpesa

Flask-Mpesa is a mpesa-py extension for flask Applications.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install flask-mpesa.

```bash
pip install Flask-Mpesa
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
This returns a json response to your result_url.

```python
@app.route('/transact/b2c')
def b2c_transact():
    data={"initiator_name": "[InitiatorName]",
            "security_credential": "[SecurityCredential]",#from developers portal
            "amount": "1000",
            "command_id":"[command_id]",
            "party_a": "[PartyA]",
            "party_b": "[PartyB]",
            "remarks": "[Remarks]",
            "queue_timeout_url": "YOUR_URL" ,
            "result_url": "YOUR_URL",
            "occassion": "[Occassion]"
    }
    mpesaapi.B2C.transact(**data)  # ** unpacks the dictionary


```

### B2B  Api
This returns a json response to your result_url.

```python
@app.route('/transact/b2b')
def b2b_transact():
    data={"initiator": "[Initiator]",
            "security_credential": "[SecurityCredential]",#from developers portal
            "amount": "1000",
            "command_id":"[command_id]",
            "sender_identifier_type":"[SenderIdentifierType]",
            "receiver_identifier_type":"[ReceiverIdentifierType]",
            "party_a": "[PartyA]",
            "party_b": "[PartyB]",
            "remarks": "[Remarks]",
            "queue_timeout_url": "YOUR_URL" ,
            "result_url": "YOUR_URL",
            "account_reference": "[AccountReference]"
    }
    mpesaapi.B2B.transact(**data)  # ** unpacks the dictionary

```

### C2B  api

```python
c2b=mpesaapi.C2B

```

### MpesaExpress  api

```python
data = {
        "business_shortcode": "[BusinessShortcode]", #from developers portal
        "passcode": "[Passcode]",#from developers portal
        "amount": "[Amount]", # choose amount preferrably KSH 1
        "phone_number":"[PhoneNumber]", #phone number to be prompted to pay
        "callback_url": "[YOUR_URL]", # cllback url should be exposes. for testing putposes you can route on host 0.0.0.0 and set the callback url to be https://youripaddress:yourport/endpoint
        "description": "[Description]" #a description of the transaction its optional
    }
    v = mpesaapi.MpesaExpress.stk_push(**data)  # ** unpacks the dictionary

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
