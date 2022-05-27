from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from EventDriven.forms.event_form import EventCreateForm, EventUpdateForm
from EventDriven.models import Event



# Create your views here.
#def start(request):
#    return render(request, 'events/indexx.html')

def index(request):
    if 'search_filter' in request.GET:
        search_filter = request.GET['searc_filter']
        events = [{
            'id': x.id,
            'name': x.name,
            'category': x.category,
            #'firstImage': c.eventimage_set.first().image #Þarf að bæta við image model-i
        } for x in Event.objects.filter(name__icontains=search_filter)]
        events = list(Event.objects.filter(name__icontains=search_filter).values() )
        return JsonResponse({ 'data': events})
    context = {'events': Event.objects.all().order_by('name')}
    return render(request, 'events/indexx.html', context )

def get_event_by_id(request, id):
    return render(request, 'events/event_details.html', {
        'event': get_object_or_404(Event, pk=id)})

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
    return render(request, 'events/create_event.html',{
        'form': form })

def delete_event(request, id):
    event = get_object_or_404(Event, pk= id)
    event.delete()
    return redirect('event-index')

def update_event(request,id):
    instance = get_object_or_404(Event,pk=id)
    if request == 'POST':
        form = EventUpdateForm(data=request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect(request,'event-details', id=id)
    else:
        form = EventUpdateForm(instance=instance)
        print(2)
    return render(request, 'events/update_event.html', {
        'form': form,
        'id': id })