from django import forms
from django.db import models
from django.forms import fields, widgets
from news.models import Article, CustomUser
from django.core.exceptions import ValidationError, ObjectDoesNotExist


class UserForm(forms.ModelForm):
	birth_date = forms.DateField(required=False, widget=forms.HiddenInput())

	class Meta:
		model = CustomUser
		fields = [
			'username',
			'password',
			'first_name',
			'last_name',
			'avatar',
			'email'
		]

		error_messages = {
			'username': {
				'unique': ('This username is already taken')
			}
		}

		widgets = {
			'username': forms.TextInput(attrs={'class': 'custom-input'}),
			'password': forms.PasswordInput(attrs={'class': 'custom-input'}),
			'first_name': forms.TextInput(attrs={'class': 'custom-input'}),
			'last_name': forms.TextInput(attrs={'class': 'custom-input'}),
			'email': forms.EmailInput(attrs={'class': 'custom-input'})
		}

	def save(self, commit=True):
		# Save the provided password in hashed format
		user = super(UserForm, self).save(commit=False)
		user.set_password(self.cleaned_data["password"])
		if commit:
			user.save()
		return user

class LoginForm(forms.Form):
	username = forms.CharField(widget=forms.TextInput(attrs={'class': 'custom-input', 'type':'text', 'placeholder': 'Username'}))
	password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'custom-input', 'type':'text', 'placeholder': 'Password'}))

	def clean(self):
		try:
			user = CustomUser.objects.get(username=self.cleaned_data['username'])
		except ObjectDoesNotExist:
			user = None

		input_password = self.cleaned_data['password']
		if user:
			if not user.check_password(input_password):
				self.add_error('password', 'Incorrect password')
		else:
			self.add_error('username', 'This username does not exist')

class ArticleForm(forms.ModelForm):
	class Meta:
		model = Article
		fields = ['article_title', 'article_text', 'hashtags']

		widgets = {
			'article_title': forms.TextInput(attrs={
				'class': 'article__title', 'type':'text', 'placeholder': 'Article title'
			}),
			'article_text': forms.Textarea(attrs={
				'class': 'article__text', 'placeholder': 'Article text', 'cols': 30, 'rows': 10, 'spellcheck': 'false'
			}),
			'hashtags': forms.TextInput(attrs={
				'class': 'article__title', 'type':'text', 'placeholder': 'Hashtags (separate with space)'
			})
		}

	def clean(self):
		self.cleaned_data['hashtags'] = self.cleaned_data['hashtags'].replace('#', '').strip()
		return super().clean()
