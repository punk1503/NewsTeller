"""newsteller URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from news import views

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
	path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', views.index, name='index'),
	path('new/', views.article_creation, name='article_creation'),
	path('article/<int:article_id>', views.article_overview, name='article_overview'),
	path('search', views.article_search, name='article_search')
]
