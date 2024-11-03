from django.shortcuts import render
from . import views

def IndexView(request):
	return render(request, 'index.html', {})
