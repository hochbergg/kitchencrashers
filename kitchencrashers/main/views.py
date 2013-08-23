# Create your views here.
from django.shortcuts import render

def home(request):
	return render(request,"index.html")

def createEvent(request):
	return render(request,"CreateEvent.html")

def showEvent(request):
	return render(request,"ShowEvent.html")