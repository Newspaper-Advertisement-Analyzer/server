from newspaper import Article

# from nlp.findlocations import extract_addresses_with_geocoding
from NLP.findlocations_new import extract_locations
from NLP.findcatogory import identify_catogory
from NLP.findprice import identify_price
from NLP.findcontacts import extract_contacts

from NLP.getPhoneNumbers import get_Phone_Numbers


def extract_article_info(url):
    # Create an Article object
    article = Article(url, language="en")  # en for English

    # To download the article
    article.download()

    # To parse the article
    article.parse()

    # To perform natural language processing (NLP)
    article.nlp()

    # Extract title
    title = article.title

    # Extract text
    text = article.text

    # Extract summary
    summary = article.summary

    # Extract keywords
    keywords = article.keywords

    # locations = extract_addresses_with_geocoding(text)
    catogory = identify_catogory(text + title)
    price = identify_price(text)
    phone = get_Phone_Numbers(text, url)
    locations = extract_locations(text + title)

    return title, text, summary, keywords, catogory, price, phone, locations
    return summary, title, text, keywords, locations, catogory, price, contact
