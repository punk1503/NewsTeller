from django import forms
from django.forms import fields
from news.models import Article

class ArticleForm(forms.ModelForm):
	class Meta:
		model = Article
		fields = ['article_header', 'artcile_text']
