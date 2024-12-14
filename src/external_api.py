import os

import requests
from dotenv import load_dotenv


load_dotenv()
API_KEY = os.getenv('API_KEY')

list_of_transactions = {
    "id": 782295999,
    "state": "EXECUTED",
    "date": "2019-09-11T17:30:34.445824",
    "operationAmount": {
      "amount": 54280.01,
      "currency": {
        "name": "евро",
        "code": "EUR"
      }
    },
    "description": "Перевод организации",
    "from": "Счет 24763316288121894080",
    "to": "Счет 96291777776753236930"
  }


def get_transaction_amount(list_of_transactions: dict) -> float:
    """Функция принимает на вход транзакцию и возвращает сумму транзакции в рублях"""
    # sum_of_amount = 0
    # for transactions in list_of_transactions:
    if "operationAmount" in list_of_transactions:
        amount = list_of_transactions["operationAmount"]["amount"]
        currency = list_of_transactions["operationAmount"]["currency"]["code"]
        if currency == "RUB":
            return float(amount)
        elif currency == "USD" or currency == "EUR":
            url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency}&amount={amount}"

            payload = {}
            headers = {"apikey": API_KEY}

            response = requests.request("GET", url, headers=headers, data=payload)
            # print(response.json())

            return float(response.json()['result'])
        else:
            raise ValueError("The currency didn't convert. Use one of this currency: RUB/USD/EUR.")


if __name__ == '__main__':
    print(get_transaction_amount(list_of_transactions))
