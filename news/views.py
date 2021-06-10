from django.shortcuts import redirect, render
from newsteller import forms
from news import models
import datetime



def index(request):
	ARTICLES_CNT = 10
	context = {
		'pagename': 'Main',
		'lattest_articles': models.Article.objects.order_by('-publication_date')[:ARTICLES_CNT]
	}
	return render(request, 'news/pages/index.html', context)


def article_creation(request):
	context = {'pagename': 'New article'}

	if request.method == 'GET':
		article_form = forms.ArticleForm()
		context['article_form'] = article_form
	elif request.method == 'POST':
		new_article = forms.ArticleForm(request.POST).save(commit=False)
		new_article.author = request.user
		new_article.publication_date = datetime.datetime.now().date()
		new_article.save()

		return redirect('index')

	return render(request, 'news/pages/article_creation.html', context)

def article_overview(request, article_id):
	context = {'pagename': 'Article'}
	article = models.Article.objects.get(id=article_id)
	context['article'] = article
	return render(request, 'news/pages/article_overview.html', context)


def registration(request):
	if request.user.is_authenticated:
		return redirect('index')
	context = {'pagename': 'Registration'}

	if request.method == 'GET':
		user_form = forms.UserForm()
	elif request.method == 'POST':
		user_form = forms.UserForm(request.POST)
		if user_form.is_valid():
			new_user = user_form.save()
			return redirect('index')

	return render(request, 'news/pages/registration.html', context)
