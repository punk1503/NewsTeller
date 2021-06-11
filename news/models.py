from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import AbstractUser, User
from django.conf import settings
import os
from django.core.exceptions import ObjectDoesNotExist


class CustomUser(AbstractUser):
	class Meta:
		verbose_name = 'Custom user'
		verbose_name_plural = 'Custom users'

	def set_avatar_path(instance, filename):
		upload_to = 'profiles'
		return os.path.join(upload_to, (f'{instance.username}_{filename}'))

	# def save(self, *args, **kwargs):
	# 	super(CustomUser, self).save(*args, **kwargs)

	avatar = models.ImageField(blank=True, null=True, upload_to=set_avatar_path)
	is_author = models.BooleanField(default=False)
	username = models.CharField(max_length=15, unique=True, verbose_name='Username')
	USERNAME_FIELD = 'username'

	REQUIRED_FIELDS = ['first_name', 'last_name', 'email']

	# TODO: add email validation to become an author

	def __str__(self) -> str:
		return self.username


class Article(models.Model):
	"""
	A model that represents news report or some article
	"""
	class Meta:
		verbose_name = 'Article'
		verbose_name_plural = 'Articles'

	article_title = models.CharField(verbose_name='Article header', max_length=100)
	article_text = models.TextField(verbose_name='Article text')
	publication_date = models.DateField(verbose_name='Publication Date')
	author = models.ForeignKey(verbose_name='Article author', to=CustomUser, on_delete=CASCADE)
	likes = models.IntegerField(verbose_name="Likes on article", default=0)
