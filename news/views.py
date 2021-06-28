from typing import ContextManager
from django.shortcuts import redirect, render
from newsteller import forms
from news import models
import datetime
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import authenticate, login
from django.http import JsonResponse

def anon_check(user):
	if user:
		return not user.is_authenticated
	return True

def index(request):
	ARTICLES_CNT = 10
	context = {
		'pagename': 'Main',
		'lattest_articles': models.Article.objects.order_by('-publication_date')[:ARTICLES_CNT]
	}
	return render(request, 'news/pages/index.html', context)

@login_required
def article_creation(request):
	context = {'pagename': 'New article'}

	if request.method == 'GET':
		context['article_form'] = forms.ArticleForm()
	elif request.method == 'POST':
		new_article = forms.ArticleForm(request.POST).save(commit=False)
		new_article.author = request.user
		new_article.publication_date = datetime.datetime.now().date()
		new_article.save()

		return redirect('index')

	return render(request, 'news/pages/article_creation.html', context)

def article_overview(request, article_id):
	context = {
		'pagename': 'Article',
		'article': models.Article.objects.get(id=article_id)
	}
	if request.method == 'POST' and request.user.is_authenticated:
		if request.user in context['article'].likers.all():
			context['article'].likers.remove(request.user)
		else:
			context['article'].likers.add(request.user)
		return JsonResponse({
			'like_counter': context['article'].likers.all().count(),
			'current_user_liked': request.user in context['article'].likers.all()
		})
	return render(request, 'news/pages/article_overview.html', context)

@user_passes_test(anon_check, redirect_field_name=None, login_url='/')
def registration(request):
	context = {'pagename': 'Registration'}

	if request.method == 'GET':
		context['user_form'] = forms.UserForm()
	elif request.method == 'POST':
		user_form = forms.UserForm(request.POST, request.FILES)
		if user_form.is_valid():
			new_user = user_form.save()
			login(request, new_user)
			return redirect('index')
		else:
			context['user_form'] = user_form
	return render(request, 'news/pages/registration.html', context)

@user_passes_test(anon_check, redirect_field_name=None, login_url='/')
def login_page(request):
	context = {'pagename': 'Sign in'}

	if request.method == 'GET':
		context['form'] = forms.LoginForm()
	elif request.method == 'POST':
		form = forms.LoginForm(request.POST)
		context['form'] = form
		if form.is_valid():
			user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
			if user is not None:
				login(request, user)
				return redirect('index')
	return render(request, 'news/pages/login.html', context)


def profile_page(request, username):
	context = {'pagename': 'Profile'}
	current_user = models.CustomUser.objects.get(username=username)
	if current_user:
		current_user_articles = models.Article.objects.filter(author=current_user)

	context['current_user'] = current_user
	context['current_user_articles'] = current_user_articles
	return render(request, 'news/pages/profile_page.html', context)
