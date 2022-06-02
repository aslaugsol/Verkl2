from django import forms
from django.forms import ModelForm, widgets
from EventDriven.models import Event, Booking


class EventUpdateForm(ModelForm ):

    class Meta:
        model = Event
        exclude = ['id']
        widgets = {
            'name': widgets.TextInput(attrs={'class': 'form-control'}),
            'date': widgets.DateInput(attrs={'class': 'form-control'}),
            'category': widgets.TextInput(attrs={'class': 'form-control'}), #Select(attrs={'class': 'form-control'}),
            'price': widgets.NumberInput(attrs={'class': 'form-control'}),
            'max_tickets': widgets.NumberInput(attrs={'class': 'form-control'}),
            'tickets_available': widgets.NumberInput(attrs={'class': 'form-control'}),

        }


class EventCreateForm(ModelForm):
    #image = forms.Charfield(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Event
        exclude = ['id']
        widgets = {
            'name': widgets.TextInput(attrs={'class': 'form-control'}),
            'date': widgets.DateInput(attrs={'class': 'form-control'}),
            'description': widgets.TextInput(attrs={'class': 'form-control'}),
            'category': widgets.Select(attrs={'class': 'form-control'}),
            'price': widgets.NumberInput(attrs={'class': 'form-control'}),
            'max_tickets': widgets.NumberInput(attrs={'class': 'form-control'}),
            'tickets_available': widgets.NumberInput(attrs={'class': 'form-control'}),

        }




class EventBookingForm(ModelForm):
    class Meta:
        model = Booking
        exclude = ['id']
        widgets = {
            'event': widgets.Select(attrs={'class': 'form-control'}),
            'quantity': widgets.NumberInput(attrs={'class': 'form-control'}),
            'delivery': widgets.Select(attrs={'class': 'form-control'}),
        }

