from django import forms
from .models import Event

class EventEnrollForm(forms.Form):
    event = forms.ModelChoiceField(queryset=Event.objects.all(),widget=forms.HiddenInput)
