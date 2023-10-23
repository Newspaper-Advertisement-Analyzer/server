from newspaper import Article

import requests
from bs4 import BeautifulSoup


def extract_article_text(url):
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

    return text




def extract_paragraphs_and_list_items(url):
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an exception for non-200 status codes

        soup = BeautifulSoup(response.text, "html.parser")

        paragraphs = [p.get_text() for p in soup.find_all("p")]
        list_items = [li.get_text() for li in soup.find_all("li")]

        text = '\n'.join(paragraphs + list_items)

        return text
    
    except requests.exceptions.RequestException as e:
        print("Error fetching the webpage:", e)
        return None


