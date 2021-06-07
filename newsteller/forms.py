from django import forms
from django.forms import fields
from news.models import Article

class ArticleForm(forms.ModelForm):
	class Meta:
		model = Article
		fields = ['article_title', 'article_text']

		widgets = {
			'article_title': forms.TextInput(attrs={'class': 'article__title', 'type':'text', 'placeholder': 'Article title'}),
			'article_text': forms.Textarea(attrs={'class': 'article__text', 'placeholder': 'Article text', 'cols': 30, 'rows': 10})
		}
