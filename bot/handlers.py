from telegram import Update
from telegram.ext import ContextTypes

from bot.ai.agent import process_message


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Olá! Eu sou a Mello Finance 🤖\n\n"
        "Estou pronta para ajudar com seus dados financeiros."
    )


async def handle_message(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):
    print("RECEBI:", update.message.text)

    response = process_message(
        update.message.text
    )

    await update.message.reply_text(response)