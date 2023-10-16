import re

def extract_phone_num(text):
    pattern1 = r'\+94\s(\d{2})\s(\d{3})\s(\d{4})'
    pattern2 = r'0(\d{2})\s(\d{3})\s(\d{4})'
    pattern3 = r'0(\d{9})'

    matches1 = re.findall(pattern1, text)
    matches2 = re.findall(pattern2, text)
    matches3 = re.findall(pattern3, text)

    phone_numbers = ['+94 ' + ''.join(match) for match in matches1]
    phone_numbers += ['0' + ''.join(match) for match in matches2]
    phone_numbers += ['0' + match for match in matches3]

    if len(phone_numbers) == 0:
        return None
    return ', '.join(phone_numbers)


# print(extract_phone_num(" Colombo-05 (off Jawatta Rd) 15.50 Parches F/Road side, Rectangle Land with 03 Houses 255 m (Negotiable) 0772456189" ))