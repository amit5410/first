from django.http import HttpResponse
from django.shortcuts import render, redirect



# Create your views here.
def homepage(request):
	#return HttpResponse('homepage')
	return render(request, 'homepage.html')

def about(request):
	#return HttpResponse('about')
	return render(request, 'about.html')

def contacts(request):
	return render(request, 'contact.html')

