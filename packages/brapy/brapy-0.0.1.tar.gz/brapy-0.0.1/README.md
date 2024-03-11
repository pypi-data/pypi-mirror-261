# Brapy

Brapy is python client to acess brapi.dev.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
pip install brapy
```

## Usage

```python
from brapy import Client

# returns a Client with 'ticker' selected
api = Client().select('ticker')

# returns prices of the 'ticker' selected
prices = api.prices()

```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)