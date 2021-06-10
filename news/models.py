from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
	class Meta:
		verbose_name = 'Custom user'
		verbose_name_plural = 'Custom users'

	birth_date = models.DateField(verbose_name='Birth date')
	avatar_blob = models.TextField(default='', blank=True, verbose_name='User profile picture blob')
	is_author = models.BooleanField(default=False)
	username = models.CharField(max_length=15, unique=True, verbose_name='Username')
	USERNAME_FIELD = 'username'

	REQUIRED_FIELDS = ['birth_date', 'first_name', 'last_name']

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
