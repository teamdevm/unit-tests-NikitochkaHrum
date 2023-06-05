import requests

class Converter:
    def get_exchange_rate(self, currency: str) -> float:
        # Метод возвращает курс указанной валюты
        # url = 'https://api.coindesk.com/v1/bpi/currentprice.json'
        if currency == 'USD':
            return 100
        elif currency == 'GBP':
            return 200
        elif currency == 'EUR':
            return 300
        return None

    def convert_bitcoins(self, currency: str, coins: int) -> float:
        # Метод возвращает сколько стоит в указанной валюте заданное количество биткоинов
        if currency == 'USD':
            return 26730*coins
        elif currency == 'GBP':
            return 21600*coins
        elif currency == 'EUR':
            return 25030*coins
        return None
    
    def convert_bitcoins_request(self, currency: str, coins: int) -> float:
        url = 'https://api.coindesk.com/v1/bpi/currentprice.json'
        response = requests.get(url)
        data = response.json()
        return float(data['bpi'][currency]['rate_float']) * coins
            
