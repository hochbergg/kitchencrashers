# Create your views here.
from django.shortcuts import render
from django.http import HttpResponseRedirect
from models import Event
import models
import django
from django.contrib.auth.decorators import login_required
from forms.event_form import EventForm
from models import RsvpOptions



def home(request):
    events = Event.objects.all()
    form = EventForm()
    return render(request,"index.html",{'events':events, 'form':form})

def login(request):
    return render(request, "registration/login.html")

def search(request):
	return render(request,"search.html")

def saveEventToDB(event_form,request):
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
    event.city = event_form.cleaned_data['city']
    event.max_people = event_form.cleaned_data['max_people']
    event.name = event_form.cleaned_data['name']

    event.organizer_id = request.user.id
    user = models.KitchenUser.objects.get(id=request.user.id)

    event.save()

    participant = models.EventParticipant(event = event, user = user, rsvp = models.RsvpOptions().\
        get_rsvp_by_id(int(event_form.cleaned_data['rsvp'])))
    participant.save()

    return event.id

@login_required()
def createEvent(request):
    if (request.method == 'POST'):
        form = EventForm(request.POST, request.FILES)
        print '******************************'
        print form.is_valid()
        print '******************************'
        if (form.is_valid()):
            id = saveEventToDB(form, request)
            return HttpResponseRedirect("/showEvent/" + str(id))
    else:
        form = EventForm()
        return render(request, "CreateEvent.html", {'form': form})

def showEvent(request, eventID):
    event = Event.objects.get(pk=eventID)
    event.cooks = event.participants.filter(rsvp=RsvpOptions().COOK).count()
    event.cleaners = event.participants.filter(rsvp=RsvpOptions().CLEANER).count()
    event.per_person = event.budget / (event.participants.count() + 1)
    return render(request, "ShowEvent.html", {'event': event})


from django.utils import simplejson
from dajaxice.decorators import dajaxice_register
from django.core import serializers

@dajaxice_register
def search_api(request,data):
    filter = simplejson.loads(data)

    q = Event.objects.all()
    for k,v in filter.iteritems():
        if k == 'location':
            q = q.filter(city=v[0])
        elif k == 'category':
            q = q.filter(category=v[0])

    all_objects = list(q)
    data = simplejson.loads(serializers.serialize('json', all_objects))
    return simplejson.dumps({'events':data, 'success':True})\
