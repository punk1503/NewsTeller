from django.contrib import admin

from .models import Article, CustomUser

admin.site.register(Article)
admin.site.register(CustomUser)
