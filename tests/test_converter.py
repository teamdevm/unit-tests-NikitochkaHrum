import pytest
import requests
import json
from app.converter import Converter

@pytest.fixture
def converter():
    return Converter()

def test_return_exchange_rate(converter):
    # Для начала тест будет проверять курс в долларах USD. 
    # будем ожидать стабильную фиктивную стоимость 100 USD. 
    exchange_rate = converter.get_exchange_rate('USD')
    assert exchange_rate == 100

    exchange_rate = converter.get_exchange_rate('GBP')
    assert exchange_rate == 200

    exchange_rate = converter.get_exchange_rate('EUR')
    assert exchange_rate == 300

    return True

def test_convert_bitcoins(converter):
    cns = converter.convert_bitcoins('USD', 1)
    assert cns == 26730

    cns = converter.convert_bitcoins('GBP', 1)
    assert cns == 21600

    cns = converter.convert_bitcoins('EUR', 1)
    assert cns == 25030

    return True

@pytest.mark.parametrize("currency, result", [
    ("USD", 100),
    ("GBP", 200),
    ("EUR", 300)
])
def test_multiple_return_exchange_rate(converter, currency, result):
    # Test the get_exchange_rate method
    exchange_rate = converter.get_exchange_rate(currency)
    assert exchange_rate == result

@pytest.mark.parametrize("currency, coins, result", [
    ("USD", 1, 26730),
    ("GBP", 1, 21600),
    ("EUR", 1, 25030)
])
def test_multiple_convert_bitcoins(converter, currency, coins, result):
    # Test the get_exchange_rate method
    cns = converter.convert_bitcoins(currency, coins)
    assert cns == result

def test_convert_bitcoins_with_mocked_api(converter, monkeypatch):

    # Mock the requests.get function using monkeypatch
    def mock_get(url):
        class MockResponse:
            def __init__(self, json_data):
                self.json_data = {"time":{"updated":"May 24, 2023 21:59:00 UTC","updatedISO":"2023-05-24T21:59:00+00:00","updateduk":"May 24, 2023 at 22:59 BST"},"disclaimer":"This data was produced from the CoinDesk Bitcoin Price Index (USD). Non-USD currency data converted using hourly conversion rate from openexchangerates.org","chartName":"Bitcoin","bpi":{"USD":{"code":"USD","symbol":"&#36;","rate":"26,356.1900","description":"United States Dollar","rate_float":26356.19},"GBP":{"code":"GBP","symbol":"&pound;","rate":"22,023.0215","description":"British Pound Sterling","rate_float":22023.0215},"EUR":{"code":"EUR","symbol":"&euro;","rate":"25,674.7771","description":"Euro","rate_float":25674.7771}}}

            
            def json(self):
                return self.json_data
    
        return MockResponse(url)

    monkeypatch.setattr(requests, "get", mock_get)

    # Test the convert_bitcoins method
    converted_amount = converter.convert_bitcoins_request("USD", 100)
    assert converted_amount == 2635619.000000

    converted_amount = converter.convert_bitcoins_request("GBP", 100)
    assert converted_amount == 2202302.15

    converted_amount = converter.convert_bitcoins_request("EUR", 100)
    assert converted_amount == 2567477.71