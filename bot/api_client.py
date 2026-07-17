import requests
from bot.config import MELLO_API_URL

def create_user(name: str, telegram_id: int):
    response = requests.post(
        f"{MELLO_API_URL}/users",
        json={
            "name": name,
            "telegram_id": telegram_id,
        },
    )

    response.raise_for_status()
    return response.json()

def get_user_by_telegram(telegram_id: int):
    response = requests.get(
        f"{MELLO_API_URL}/users/telegram/{telegram_id}"
    )

    response.raise_for_status()
    return response.json()


def create_transaction(
    user_id: int,
    account_id: int,
    category_id: int,
    description: str,
    amount: float,
    transaction_type: str,
):
    response = requests.post(
        f"{MELLO_API_URL}/transactions",
        json={
            "user_id": user_id,
            "account_id": account_id,
            "category_id": category_id,
            "description": description,
            "amount": amount,
            "transaction_type": transaction_type,
        },
    )

    response.raise_for_status()
    return response.json()

def create_account(user_id: int):
    response = requests.post(
        f"{MELLO_API_URL}/accounts",
        json={
            "user_id": user_id,
            "account_type": "Conta Corrente",
            "bank_name": "Mello"
        }
    )

    response.raise_for_status()
    return response.json()