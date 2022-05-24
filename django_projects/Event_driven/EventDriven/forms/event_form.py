from django.forms import ModelForm
from EventDriven.models import Event

class EventCreateForm(ModelForm):
    class meta:
        model = Event