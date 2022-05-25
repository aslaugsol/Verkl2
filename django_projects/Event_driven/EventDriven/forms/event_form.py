from django import forms
from django.forms import ModelForm, widgets
from EventDriven.models import Event


class EventCreateForm(ModelForm):
    image = forms.Charfield(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class meta:
        model = Event
        exclude = ['id']
        widgets = {
            'name': widgets.TextInput(attrs={'class': 'form-control'}),
            'date': widgets.TextInput(attrs={'class': 'form-control'}),
            'category': widgets.Select(attrs={'class': 'form-control'}),
            'price': widgets.NumberInput(attrs={'class': 'form-control'}),
            'max_tickets': widgets.NumberInput(attrs={'class': 'form-control'}),
            'tickets_available': widgets.NumberInput(attrs={'class': 'form-control'}),

        }
