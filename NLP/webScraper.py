from newspaper import Article

# from nlp.findlocations import extract_addresses_with_geocoding
from NLP.findlocations_new import extract_locations
from NLP.findcatogory import identify_catogory
from NLP.findprice import identify_price
from NLP.findcontacts import extract_contacts
from NLP.extractEmails import extract_emails
from NLP.getPhoneNumbers import get_Phone_Numbers


def extract_url(url):
    # Create an Article object
    article = Article(url, language="en")  # en for English

    # To download the article
    article.download()

    # To parse the article
    article.parse()

    # To perform natural language processing (NLP)
    article.nlp()

    # # Extract title
    # title = article.title

    # # Extract text
    # text = article.text

    # # Extract summary
    # summary = article.summary

    # # Extract keywords
    # keywords = article.keywords
    # authors = article.authors

    # date = article.publish_date

    # # locations = extract_addresses_with_geocoding(text)
    # catogory = identify_catogory(text + title)
    # price = identify_price(text)
    # phone = get_Phone_Numbers(text, url)
    # email = extract_emails(text)
    # locations = extract_locations(text + " " + title)

    return article
    # return title, text, summary, keywords, catogory, price, phone, locations, email, None, date
    # return summary, title, text, keywords, locations, catogory, price, contact


def extract_category(article):
    title = article.title

    text = article.text

    catogory = identify_catogory(text + title)
    return catogory


def extract_article_info(article, url):
    # Extract title
    title = article.title

    # Extract text
    text = article.text

    # Extract summary
    summary = article.summary

    # Extract keywords
    keywords = article.keywords
    authors = article.authors

    date = article.publish_date

    # locations = extract_addresses_with_geocoding(text)
    catogory = identify_catogory(text + title)
    price = identify_price(text)
    phone = list(get_Phone_Numbers(text, url))
    email = extract_emails(text)
    locations = extract_locations(text + " " + title)

    return title, text, summary, keywords, catogory, price, phone, locations, email, None, date
