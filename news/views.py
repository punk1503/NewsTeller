from news.models import Article
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.shortcuts import redirect
from newsteller.forms import ArticleForm
import datetime


def index(request):
	ARTICLES_CNT = 10
	context = {
		'pagename': 'Main',
		'lattest_articles': Article.objects.order_by('-publication_date')[:ARTICLES_CNT]
	}
	return render(request, 'news/pages/index.html', context)


def article_creation(request):
	context = {'pagename': 'New article'}

	if request.method == 'GET':
		article_form = ArticleForm()
		context['article_form'] = article_form
	elif request.method == 'POST':
		new_article = ArticleForm(request.POST).save(commit=False)
		new_article.author = request.user
		new_article.publication_date = datetime.datetime.now().date()
		new_article.save()

		return redirect('index')

	return render(request, 'news/pages/article_creation.html', context)

def article_overview(request, article_id):
	context = {'pagename': 'Article'}
	article = Article.objects.get(id=article_id)
	context['article'] = article
	return render(request, 'news/pages/article_overview.html', context)
