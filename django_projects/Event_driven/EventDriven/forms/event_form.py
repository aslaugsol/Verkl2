from django import forms
from django.forms import ModelForm, widgets
from EventDriven.models import Event, Booking, PaymentInfo, Address, CountryField


class EventUpdateForm(ModelForm):
    class Meta:
        model = Event
        exclude = ['id']
        widgets = {
            'name': widgets.TextInput(attrs={'class': 'form-control'}),
            'date': widgets.DateInput(attrs={'class': 'form-control'}),
            'category': widgets.TextInput(attrs={'class': 'form-control'}),  # Select(attrs={'class': 'form-control'}),
            'price': widgets.NumberInput(attrs={'class': 'form-control'}),
            'max_tickets': widgets.NumberInput(attrs={'class': 'form-control'}),
            'tickets_available': widgets.NumberInput(attrs={'class': 'form-control'}),

        }


class EventCreateForm(ModelForm):
    # image = forms.Charfield(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))

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



class BookingCheckoutForm(ModelForm):
    class Meta:
        model = PaymentInfo
        exclude = ['id']
        widgets = {
            'user_name': widgets.TextInput(attrs={'class': 'form-control'}),
            'card_number': widgets.NumberInput(attrs={'class': 'form-control'}),
            'cvc': widgets.NumberInput(attrs={'class': 'form-control'}),
            'expiration_month': widgets.NumberInput(attrs={'class': 'form-control'}),
            'expiration_year': widgets.NumberInput(attrs={'class': 'form-control'}),
        }


class AddressCheckoutForm(ModelForm):
    class Meta:
        model = Address
        exclude = ['id']
        widgets = {
            'full_name': widgets.TextInput(attrs={'class': 'form-control'}),
            'street_name': widgets.TextInput(attrs={'class': 'form-control'}),
            'house_no': widgets.TextInput(attrs={'class': 'form-control'}),
            'postal_code': widgets.NumberInput(attrs={'class': 'form-control'}),
            'city': widgets.TextInput(attrs={'class': 'form-control'}),
            'country': widgets.TextInput(attrs={'class': 'form-control'}),
        }
