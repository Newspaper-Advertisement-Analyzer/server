import re

def extract_phone_num(text):
    pattern = r'(?:(\+94|\b0)\s?)?(\d{2})\s?(\d{3})\s?(\d{4}|\d{5})'

    matches = re.findall(pattern, text)

    phone_numbers = []

    for match in matches:
        country_code, area_code, first_part, second_part = match
        full_number = f"{country_code or '0'}{area_code} {first_part} {second_part}"
        phone_numbers.append(full_number)

    if not phone_numbers:
        return None

    return ', '.join(phone_numbers)

