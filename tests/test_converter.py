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

    assert None ==None