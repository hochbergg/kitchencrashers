from django import forms
from django.contrib.admin import widgets

class EventForm(forms.Form):
    """
    This is a form
    """

    # def __init__(self, *args, **kwargs):
    #     super(EventForm, self).__init__(*args, **kwargs)
    #     self.fields['date'].widget.attrs['class'] = 'datepicker'

    name = forms.CharField()
    date = forms.DateTimeField()
    location = forms.CharField()
    category = forms.CharField()
    description = forms.CharField()
    budget = forms.IntegerField()
    max_people = forms.IntegerField()
    is_vegan = forms.BooleanField(required=False)
    is_kosher = forms.BooleanField(required=False)
    is_vegeterian = forms.BooleanField(required=False)
    picture = forms.ImageField(required=False)
