from django import forms
from django.db import models
from django.forms import fields, widgets
from news.models import Article, CustomUser

class UserForm(forms.ModelForm):
	class Meta:
		model = CustomUser
		fields = [
			'username',
			'password',
			'first_name',
			'last_name',
			'birth_date',
			'avatar_blob',
			'email'
		]

		widgets = {
			'avatar_blob': forms.HiddenInput(attrs={'id': 'avatar_input'}),
		}

class ArticleForm(forms.ModelForm):
	class Meta:
		model = Article
		fields = ['article_title', 'article_text']

		widgets = {
			'article_title': forms.TextInput(attrs={'class': 'article__title', 'type':'text', 'placeholder': 'Article title'}),
			'article_text': forms.Textarea(attrs={'class': 'article__text', 'placeholder': 'Article text', 'cols': 30, 'rows': 10})
		}
