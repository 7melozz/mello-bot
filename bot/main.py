from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    filters
)

from bot.config import TELEGRAM_TOKEN
from bot.handlers import start, handle_message


def main():
    app = Application.builder().token(TELEGRAM_TOKEN).build()

    app.add_handler(
        CommandHandler("start", start)
    )

    app.add_handler(
        MessageHandler(
            filters.TEXT & ~filters.COMMAND,
            handle_message
        )
    )

    print("Mello Bot iniciado 🚀")

    app.run_polling()


if __name__ == "__main__":
    main()