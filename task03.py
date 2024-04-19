import re

raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

def normalize_phone(num):
    pattern = r"[^0-9+]"
    cleaned_number = re.sub(pattern, "", num)

    if cleaned_number.startswith("380"):
        return "+" + cleaned_number
    elif cleaned_number.startswith("+"):
        return cleaned_number
    else:
        return "+38" + cleaned_number

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)