import json
import requests
from config import *

class ConvException(Exception):
    pass

class Convertor:
    @staticmethod
    def get_price(values):
        if len(values) != 3:
            raise ConvException(f'Неверное количество параметров')
        curr1, curr2, amount = values
        if curr1 == curr2:
            raise ConvException(f'Одинаковые валюты {curr2}')

        try:
            curr1_formatted = keys[curr1]
        except KeyError:
            raise ConvException(f'Не удалось обработать валюту {curr1}')

        try:
            curr2_formatted = keys[curr2]
        except KeyError:
            raise ConvException(f'Не удалось обработать валюту {curr2}')

        try:
            amount = float(amount)
        except ValueError:
            raise ConvException(f'Не удалось обработать количество {amount}')

        url = f'http://api.exchangeratesapi.io/latest?base={curr1_formatted}&symbols={curr2_formatted}'
        r = requests.get(url)
        result = float(json.loads(r.content)['rates'][keys[curr2]]) * amount
        return round(result, 3)

