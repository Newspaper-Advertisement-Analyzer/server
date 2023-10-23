from NLP.oldwebScaper import extract_paragraphs_and_list_items
from NLP.extractPhoneNumbers import extract_phone_num

def get_Phone_Numbers(text,url):

    print("this get phone numeber is running")
    print("text is ",text)
    if extract_phone_num(text) is not None:
        return extract_phone_num(text)
    else:
        print("Doing webScraping")
        new_text = extract_paragraphs_and_list_items(url)
        if extract_phone_num(new_text) is not None:
            return extract_phone_num(new_text)
        else:
            return "No phone number found"

