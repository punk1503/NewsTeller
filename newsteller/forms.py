from django import forms
from django.forms import fields
from news.models import Article

class ArticleForm(forms.ModelForm):
	class Meta:
		model = Article
		fields = ['article_title', 'article_text']

		widgets = {
			'article_title': forms.TextInput(),
			'article_text': forms.Textarea(attrs={'cols': 30, 'rows': 5})
		}
