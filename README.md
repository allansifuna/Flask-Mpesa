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

##if you are using blueprints
```python
from flask_mpesa import MpesaAPI
mpesaapi=MpesaAPI()

mpesaapi.init_app(app)
```
## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
## Tests and Examples

Examples are comming soon!.
## License
[MIT](https://choosealicense.com/licenses/mit/)
