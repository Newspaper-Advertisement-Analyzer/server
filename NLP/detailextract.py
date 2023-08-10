import spacy
# import phonenumbers
import re
from NLP.getPhoneNumbers import extract_phone_num
from NLP.getPrices import extract_price
from NLP.webScaper import extract_paragraphs_and_list_items
from NLP.webScaper import extract_article_text

# Uncomment the line below if you haven't downloaded the model already
#spacy.cli.download("en_core_web_sm")

NER = spacy.load("en_core_web_sm")

# def extract_phone_numbers(text):
#     phone_numbers = []
#     for match in phonenumbers.PhoneNumberMatcher(text, "LK"):  # Assuming Sri Lankan phone numbers for this example
#         phone_numbers.append(phonenumbers.format_number(match.number, phonenumbers.PhoneNumberFormat.E164))
#     return phone_numbers

def extract_email_addresses(text):
    return re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', text)

# def extract_prices(text):
#     # Add your custom rules or regular expressions to extract prices here
#     # Example: regex to extract prices in the format "Rs 123.45 mn"
#     return re.findall(r'Rs\s*(\d+(\.\d{1,2})?)\s*mn', text)

def categorize_advertisement(advertisement_text):
    category = None

    # Check for common keywords to categorize the advertisement
    keywords_to_category = {
        "landsales": ["land for sale", "landsales", "land plot", "property for sale", "land for"],
        "marriage_proposals": ["marriage proposal", "bride", "groom", "marriage partner"],
        "vehicle_for_sale": ["vehicle for sale", "car for sale", "auto for sale", "motorcycle for sale"]
    }

    lowercased_text = advertisement_text.lower()
    for cat, keywords in keywords_to_category.items():
        if any(keyword in lowercased_text for keyword in keywords):
            category = cat
            break

    return category



def analyze_advertisement(advertisement_URL):
    advertisement_text = extract_article_text(advertisement_URL)

    entities = NER(advertisement_text).ents
    location = None
    category = categorize_advertisement(advertisement_text)
    contact_info = {
        "phone_numbers": [],
        "email_addresses": []
    }

    
    for ent in entities:
        if ent.label_ == 'GPE':  # GPE label indicates locations
            location = ent.text.strip()

    if extract_phone_num(advertisement_text) is not None:
        contact_info["phone_numbers"] = extract_phone_num(advertisement_text)
    else:
        print("Doing webScraping")
        new_text = extract_paragraphs_and_list_items(advertisement_URL)
        if extract_phone_num(new_text) is not None:
            contact_info["phone_numbers"] = extract_phone_num(new_text)
        else:
            contact_info["phone_numbers"] = ["No phone number found"]

    if extract_price(advertisement_text) is not None:
        prices = extract_price(advertisement_text)
    else:
        print("Doing webScraping")
        new_text = extract_paragraphs_and_list_items(advertisement_URL)
        if extract_price(new_text) is not None:
            prices = extract_price(new_text)
        else:
            "No price found"

    contact_info["phone_numbers"] = extract_phone_num(advertisement_text)




    contact_info["email_addresses"] = extract_email_addresses(advertisement_text)

    return location, category, contact_info, prices
