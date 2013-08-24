# Create your views here.
from django.shortcuts import render
from django.http import HttpResponseRedirect
from models import Event
import models
import django
from forms.event_form import EventForm

COOK = 'Cook'
CLEANER = 'Cleaner'


def home(request):
    return render(request, "index.html")

def saveEventToDB(event_form):
    event = Event()
    event.budget = event_form.cleaned_data['budget']
    event.category = event_form.cleaned_data['category']
    event.date = event_form.cleaned_data['date']
    event.description = event_form.cleaned_data['description']
    event.is_kosher = event_form.cleaned_data['is_kosher']
    event.is_vegan = event_form.cleaned_data['is_vegan']
    event.is_vegeterian = event_form.cleaned_data['is_vegeterian']
    event.picture = event_form.cleaned_data['picture']
    event.location = event_form.cleaned_data['location']
    event.max_people = event_form.cleaned_data['max_people']
    event.name = event_form.cleaned_data['name']
    
    event.organizer_id = 2 #shouldnt be hardcoded
    event.save()
    return event.id

def createEvent(request):
    if (request.method == 'POST'):
        form = EventForm(request.POST)
        if (form.is_valid()):
            saveEventToDB(form)
            redirect_page = "/showEvent/" + str(id) + "/"
            return HttpResponseRedirect(redirect_page)
    else:
        form = EventForm()
    return render(request, "CreateEvent.html", {'form': form})

def showEvent(request, eventID):
    event = Event.objects.get(pk=eventID)
    event.cooks = event.participants.filter(rsvp=COOK).count()
    event.cleaners = event.participants.filter(rsvp=CLEANER).count()
    event.per_person = event.budget / (event.participants.count() + 1)
    return render(request, "ShowEvent.html", {'event': event})