import re


def parse_message(message: str):

    text = message.lower()

    if "gastei" in text or "gasto" in text:
        numbers = re.findall(r"\d+", text)

        if numbers:
            amount = float(numbers[0])

            description = (
                text
                .replace("gastei", "")
                .replace("gasto", "")
                .strip()
            )

            return {
                "intent": "expense",
                "amount": amount,
                "description": description
            }


    return {
        "intent": "unknown",
        "message": message
    }
