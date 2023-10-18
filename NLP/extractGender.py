import re


gender = re.findall("female|gentleman|woman|man|girl|boy", your_text)

gender_dict = {"male": ["gentleman", "man", "male"],
               "female": ["female", "woman", "girl"]}
gender_aux = []
for g in gender:
    if g in gender_dict['male']:
        gender_aux.append('male')
    elif g in gender_dict['female']:
        gender_aux.append('female')