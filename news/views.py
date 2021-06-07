from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.shortcuts import redirect
from newsteller.forms import ArticleForm
import datetime


def index(request):
	return render(request, 'news/pages/index.html')

def article_creation(request):
	context = {}
	if request.method == 'GET':
		article_form = ArticleForm()
		context['article_form'] = article_form
	elif request.method == 'POST':
		new_article = ArticleForm(request.POST)
		new_article.author = request.user
		new_article.publication_date = datetime.datetime.now().date()
		new_article.save()

		return redirect('index')

	return render(request, 'news/pages/article_creation.html', context)

