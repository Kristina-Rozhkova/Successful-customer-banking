import os

import requests
from dotenv import load_dotenv

from src.utils import get_financial_transactions

load_dotenv()
API_KEY = os.getenv('API_KEY')

list_of_transactions = get_financial_transactions(r"..\data\operations1.json")


def get_transaction_amount(list_of_transactions: list) -> float:
    """Функция принимает на вход транзакцию и возвращает сумму транзакции в рублях"""
    # sum_of_amount = 0
    for transactions in list_of_transactions:
        if "operationAmount" in transactions:
            amount = transactions["operationAmount"]["amount"]
            currency = transactions["operationAmount"]["currency"]["code"]
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
