from django.http import HttpResponse
from django.shortcuts import render, redirect
from EventDriven.forms.event_form import EventCreateForm
from EventDriven.models import Event



# Create your views here.
#def start(request):
#    return render(request, 'events/indexx.html')

def index(request):
    context = {'events': Event.objects.all().order_by('name')}
    return render(request, 'events/indexx.html', context )

def create_event(request):
    if request.method == 'POST':
        form = EventCreateForm(data=request.POST)
        if form.is_valid():
             event = form.save()
             event_img = EventImage(image=request.POST['image'], event=event)
             event_img.save()
             return redirect('event-index')
    else:
        form = EventCreateForm()
        # TODO: Instance new EventCreateForm()
    return render(request, 'EventDriven/create_event.html',{
        'form': form })