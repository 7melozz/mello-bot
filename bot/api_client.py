import requests

from bot.config import MELLO_API_URL


def create_user(name, telegram_id):
    response = requests.post(
        f"{MELLO_API_URL}/users",
        params={
            "name": name,
            "telegram_id": telegram_id
        }
    )

    response.raise_for_status()

    return response.json()