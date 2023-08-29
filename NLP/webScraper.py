from newspaper import Article

# from nlp.findlocations import extract_addresses_with_geocoding
from NLP.findlocations_new import extract_locations
from NLP.findcatogory import identify_catogory
from NLP.findprice import identify_price
from NLP.findcontacts import extract_contacts



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
    locations = extract_locations(text)
    catogory = identify_catogory(text)
    price = identify_price(text)
    contact = extract_contacts(text)


    return title, text, summary, keywords, catogory, price, contact, locations
    return summary, title, text, keywords, locations, catogory, price, contact
