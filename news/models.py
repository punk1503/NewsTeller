from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User


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
    author = models.ForeignKey(verbose_name='Article author', to=User, on_delete=CASCADE)
    likes = models.IntegerField(verbose_name="Likes on article", default=0)
