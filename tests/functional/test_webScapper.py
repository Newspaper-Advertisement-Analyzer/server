from NLP import webScraper


def test_extract_article_info():
    # Replace the URL with a valid article URL
    url = "https://www.hitad.lk/en/ad/1779332-Kalubowila-House-for-Sale?type=houses"
    title, text, summary, keywords, catogory, price, contact, locations = webScraper.extract_article_info(
        url)

    assert isinstance(title, str)
    assert isinstance(text, str)
    assert isinstance(summary, str)
    assert isinstance(keywords, list)
    assert isinstance(catogory, str)
    assert isinstance(price, tuple)
    assert isinstance(contact, list)
    assert isinstance(locations, list)

    # Add more assertions based on the expected behavior of the 'extract_article_info' function
