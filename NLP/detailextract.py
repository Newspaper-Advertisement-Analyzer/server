import spacy

import re
from NLP.getPhoneNumbers import get_Phone_Numbers
from NLP.getPrices import extract_price
from NLP.getLocations import extract_locations
from NLP.oldwebScaper import extract_paragraphs_and_list_items
from NLP.oldwebScaper import extract_article_text
from NLP.findprice import identify_price
from NLP.findlocations_new import extract_locations
from NLP.findcatogory import categorize_advertisement

from NLP.extractPhoneNumbers import extract_phone_num

# Uncomment the line below if you haven't downloaded the model already
#spacy.cli.download("en_core_web_sm")

NER = spacy.load("en_core_web_sm")


# def extract_email_addresses(text):
#     return re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', text)


def analyze_advertisement(advertisement_URL):
    advertisement_text = extract_article_text(advertisement_URL)

    category = categorize_advertisement(advertisement_text)

    contact_info = {
        "phone_numbers": [],
        "email_addresses": []
    }
    
    print("phone numerb is going to run"    )
    contact_info["phone_numbers"] = get_Phone_Numbers(advertisement_text,advertisement_URL)


    if extract_price(advertisement_text) is not None:
        prices = extract_price(advertisement_text)
    else:
        print("Doing webScraping")
        new_text = extract_paragraphs_and_list_items(advertisement_URL)
        if extract_price(new_text) is not None:
            prices = extract_price(new_text)
        else:
            prices = ["No price found"]

    location = extract_locations(advertisement_text)

    print("Location: ", location)
    print("Category: ", category)
    print("Contact info: ", contact_info)
    print("Prices: ", prices)

    return location, category, contact_info, prices

def analyze_advertisement_img(advertisement_text):

    location = extract_locations(advertisement_text)
    
    category = categorize_advertisement(advertisement_text)
    contact_info = []

    if extract_phone_num(advertisement_text) is not None:
        contact_info = extract_phone_num(advertisement_text)
    else:
        contact_info= ["No phone number found"]

    if  identify_price(advertisement_text) is not None:
        prices =  identify_price(advertisement_text)
    else:
       prices = ["No price found"]


    print("Location: ", location)
    print("Category: ", category)
    print("Contact info: ", contact_info)
    print("Prices: ", prices)

    return location, category, contact_info, prices
