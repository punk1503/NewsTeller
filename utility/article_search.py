from news.models import Article

def match_articles(article_title: str):
	# getting words bigger than 3 letters
	title_words = [word for word in article_title.split() if len(word) >= 3]
