from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.shortcuts import redirect


def index(request):
	return render(request, 'news/pages/index.html')
