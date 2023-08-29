import re


def extract_phone_num(text):
    # Regular expression patterns to match phone numbers
    pattern1 = r'\+94\s(\d{2})\s(\d{3})\s(\d{4})'
    pattern2 = r'0(\d{2})\s(\d{3})\s(\d{4})'
    pattern3 = r'0(\d{9})'

    # Find all matches of phone numbers in the text
    matches1 = re.findall(pattern1, text)
    matches2 = re.findall(pattern2, text)
    matches3 = re.findall(pattern3, text)

    # Combine the matched groups to form complete phone numbers
    phone_numbers = ['+94 ' + ''.join(match) for match in matches1]
    phone_numbers += ['0' + ''.join(match) for match in matches2]
    phone_numbers += ['0' + match for match in matches3]

    if len(phone_numbers) == 0:
        return None
    return phone_numbers


#________Test___________________________
# print(extract_phone_num(" for Three Vehicles, Pantry, Wet Kitchen. 33 M 0773033852."))