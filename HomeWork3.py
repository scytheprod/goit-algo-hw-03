import re

def normalize_phone(phone_number):
    pattern = r"\D"
    corrected_num = re.sub(pattern,"", phone_number)
    if corrected_num.startswith("0"):
        corrected_num = "380" + corrected_num[1:]
    elif corrected_num.startswith("8"):
        corrected_num = "380" + corrected_num[1:]
    elif corrected_num.startswith("380"):
        pass
    else:
        corrected_num = "380" + corrected_num
    return f"+{corrected_num}"
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
    "0664801622"
]
sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)
