import floppyforms as forms
from kitchencrashers.main.models import RsvpOptions
from kitchencrashers.main.models import CategoryOptions


class EventForm(forms.Form):

    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'name your event'}))
    date = forms.DateTimeField(widget=forms.SplitDateTimeWidget)
    location = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'address'}))
    city = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'city'}))
    category = forms.ChoiceField(choices=CategoryOptions().CATEGORY_OPTIONS)
    description = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'don\'t be shy - tell us about it some more'}))
    budget = forms.IntegerField()
    max_people = forms.IntegerField()
    is_vegan = forms.BooleanField(required=False)
    is_kosher = forms.BooleanField(required=False)
    is_vegeterian = forms.BooleanField(required=False)
    rsvp = forms.ChoiceField(widget=forms.RadioSelect, choices=RsvpOptions().RSVP_OPTIONS)
    picture = forms.ImageField()
