import os
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
MELLO_API_URL = os.getenv("MELLO_API_URL")

if not TELEGRAM_TOKEN:
    raise ValueError("TELEGRAM_TOKEN não encontrado")

if not MELLO_API_URL:
    raise ValueError("MELLO_API_URL não encontrado")
