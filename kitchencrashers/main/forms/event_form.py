import floppyforms as forms


class EventForm(forms.Form):

    name = forms.CharField()
    date = forms.DateTimeField(widget=forms.SplitDateTimeWidget)
    location = forms.CharField()
    category = forms.CharField()
    description = forms.CharField()
    budget = forms.IntegerField()
    max_people = forms.IntegerField()
    is_vegan = forms.BooleanField(required=False)
    is_kosher = forms.BooleanField(required=False)
    is_vegeterian = forms.BooleanField(required=False)
    picture = forms.ImageField()
