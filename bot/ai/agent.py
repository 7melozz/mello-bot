from bot.ai.parser import parse_message


def process_message(message: str):

    data = parse_message(message)

    if data["intent"] == "expense":

        return (
            f"Entendi seu gasto de "
            f"R$ {data['amount']:.2f} "
            f"com {data['description']}"
        )

    return (
        "Ainda estou aprendendo 🤖\n"
        "Tente algo como:\n"
        "'gastei 50 mercado'"
    )