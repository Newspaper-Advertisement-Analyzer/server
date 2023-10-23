
import re


def extract_contacts(text):

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
        return "No contacts found"
    return phone_numbers


# test
# print(extract_contacts("My number is +94 77 123 4567 and my friend's number is 077 123 4567 , HOMAGAMA, Pitipana, Mawathgama Road, 2 roomed, living, bathroom, kitchen with pantry, parking space for one vehicle, parapet wall surrounded, ground floor. Rs.30,000/- 0777607539"))
