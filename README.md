[![Requirements Status](https://requires.io/github/allansifuna/Flask-Mpesa/requirements.svg?branch=master)](https://requires.io/github/allansifuna/Flask-Mpesa/requirements/?branch=master)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/95668732c0014077abf06e7826c1becf)](https://www.codacy.com/manual/allansifuna/Flask-Mpesa?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=allansifuna/Flask-Mpesa&amp;utm_campaign=Badge_Grade)
[![Coverage Status](https://coveralls.io/repos/github/allansifuna/Flask-Mpesa/badge.svg?branch=master)](https://coveralls.io/github/allansifuna/Flask-Mpesa?branch=master)
![Top language](https://img.shields.io/github/languages/top/allansifuna/Flask-Mpesa)
![Code size](https://img.shields.io/github/languages/code-size/allansifuna/Flask-Mpesa?color=dark-green)
![GitHub](https://img.shields.io/github/license/allansifuna/Flask-Mpesa?color=dark-green)
![PyPI](https://img.shields.io/pypi/v/Flask-Mpesa)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/Flask-Mpesa?color=dark-green)
![PyPI - Implementation](https://img.shields.io/pypi/implementation/Flask-Mpesa?color=blue)
![PyPI - Status](https://img.shields.io/pypi/status/Flask-Mpesa)
# Flask-Mpesa
Flask-Mpesa provides a simple intergration for flask Applications with Mpesa Daraja API.

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


mpesa_api=MpesaAPI(app)
```


## if you are using blueprints
```python
from flask_mpesa import MpesaAPI
mpesa_api=MpesaAPI()

mpesa_api.init_app(app)
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
@app.route('/transact/b2c',methods=['GET'])
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
    mpesa_api.B2C.transact(**data)  # ** unpacks the dictionary


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
    mpesa_api.B2B.transact(**data)  # ** unpacks the dictionary

```

### C2B  api

```python
@app.route('/transact/c2b')
def c2b_transact():
    reg_data={"shortcode": "600364",
          "response_type": "Completed",
          "confirmation_url": "https://example.com/confirmation",
          "validation_url": "https://example.com/validation"
    }
    v=mpesa_api.C2B.register(**reg_data)  # ** unpacks the dictionary
    ##use v to capture the response


    #This method allows you to test a mock payment and see the result so it can be avoided in production mode.
    test_data={"shortcode": "600364",
           "command_id": "CustomerPayBillOnline",
           "amount": "100",
           "msisdn": "254708374149",
           "bill_ref_number": "account"
    }
    new_v = mpesa_api.C2B.simulate(**test_data)  # ** unpacks the dictionary
    #use new_v to capture the response
    return render_template('home.html')

@app.route('/confirmation',methods=["POST"])
def c2b_confirmation():
    #save the data
    request_data = request.data

    #Perform your processing here e.g. print it out...
    print(request_data)

```

### MpesaExpress  api

```python
@app.route('/transact/c2b')
def c2b_transact():
    data = {
        "business_shortcode": "[BusinessShortcode]", #from developers portal
        "passcode": "[Passcode]",#from developers portal
        "amount": "[Amount]", # choose amount preferrably KSH 1
        "phone_number":"[PhoneNumber]", #phone number to be prompted to pay
        "reference_code": "[Reference Code]",#Code to inform the user of services he/she is paying for.
        "callback_url": "[YOUR_URL]", # cllback url should be exposes. for testing putposes you can route on host 0.0.0.0 and set the callback url to be https://youripaddress:yourport/endpoint
        "description": "[Description]" #a description of the transaction its optional
    }
    resp = mpesa_api.MpesaExpress.stk_push(**data)  # ** unpacks the dictionary
    ##use resp to capture the response
    return render_template('home.html')

@app.route('/callback-url',methods=["POST"])
def callback_url():
    #get json data set to this route
    json_data = request.get_json()
    #get result code and probably check for transaction success or failure
    result_code=json_data["Body"]["stkCallback"]["ResultCode"]
    message={
        "ResultCode":0,
        "ResultDesc":"success",
        "ThirdPartyTransID":"h234k2h4krhk2"
    }
    #if result code is 0 you can proceed and save the data else if its any other number you can track the transaction
    return jsonify(message),200

```
### Balance  api

```python
balance=mpesa_api.Balance

```
### Reversal  api

```python
reversal=mpesa_api.Reversal

```
### TransactionStatus  api

```python
transaction_status=mpesa_api.TransactionStatus

```
## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
## Tests and Examples

Examples are comming soon!.
## License
[MIT](https://github.com/allansifuna/Flask-Mpesa/blob/master/LICENSE)
