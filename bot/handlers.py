from telegram import Update
from telegram.ext import ContextTypes

import requests

from bot.ai.agent import process_message
from bot.api_client import (
    get_user_by_telegram,
    create_user,
    create_account,
    create_transaction,
)
from bot.config import OWNER_ID


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    telegram_id = update.effective_user.id
    name = update.effective_user.first_name

    try:
        user = get_user_by_telegram(telegram_id)

        if telegram_id == OWNER_ID:
            await update.message.reply_text(
                "Bem-vindo de volta, Melo, my owner goat 🐐🔥"
            )
        else:
            await update.message.reply_text(
                f"Bem-vindo de volta, {user['name']}! 👋"
            )

    except requests.HTTPError as e:

        if e.response.status_code == 404:

            user = create_user(
                name=name,
                telegram_id=telegram_id,
            )

            create_account(
                user_id=user["user_id"]
            )

            await update.message.reply_text(
                "🎉 Cadastro realizado com sucesso!\n\n"
                "Sua conta financeira foi criada."
            )

        else:
            raise


async def handle_message(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    try:
        telegram_id = update.effective_user.id
        message = update.message.text

        print("Telegram ID:", telegram_id)
        print("Mensagem:", message)

        user = get_user_by_telegram(telegram_id)

        print("USUÁRIO:", user)

        response = process_message(message)

        await update.message.reply_text(response)

    except Exception as e:
        print("ERRO:", repr(e))
        await update.message.reply_text(
            f"Erro: {e}"
        )