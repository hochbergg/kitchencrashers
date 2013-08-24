import floppyforms as forms
from kitchencrashers.main.models import RsvpOptions

class EventForm(forms.Form):

    name = forms.CharField()
    date = forms.DateTimeField(widget=forms.SplitDateTimeWidget)
    location = forms.CharField()
    city = forms.CharField()
    category = forms.CharField()
    description = forms.CharField()
    budget = forms.IntegerField()
    max_people = forms.IntegerField()
    is_vegan = forms.BooleanField(required=False)
    is_kosher = forms.BooleanField(required=False)
    is_vegeterian = forms.BooleanField(required=False)
    rsvp = forms.ChoiceField(widget=forms.RadioSelect, choices=RsvpOptions().RSVP_OPTIONS)
    picture = forms.ImageField()
