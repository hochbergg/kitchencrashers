# Create your views here.
from django.shortcuts import render
from models import Event

COOK = 'Cook'
CLEANER = 'Cleaner'

def home(request):
	return render(request,"index.html")

def createEvent(request):
	return render(request,"CreateEvent.html")

def showEvent(request,eventID):
	event = Event.objects.get(pk=eventID)
	event.cooks = event.participants.filter(rsvp=COOK).count()
	event.cleaners = event.participants.filter(rsvp=CLEANER).count()
	event.per_person = event.budget / (event.participants.count() + 1)
	return render(request,"ShowEvent.html",{'event':event})