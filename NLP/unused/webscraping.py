from newspaper import Article

def scrape_article_data(inp):
    if inp.strip():  # Check if inp is not empty
        toi_article = Article(inp, language="en")
        toi_article.download()
        toi_article.parse()
        #toi_article.nlp()

        """return {
            "authors": toi_article.authors,
            "summary": toi_article.summary
        }"""
        return toi_article.text
    else:
        return None
