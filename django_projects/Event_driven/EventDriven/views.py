from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from EventDriven.forms.event_form import EventCreateForm, EventBookingForm
from EventDriven.models import Event, Category, Booking, Customer, User
import json
from django.contrib.auth.decorators import login_required


# Create your views here.
# def start(request):
#    return render(request, 'events/indexx.html')


def index(request):
    if 'search_filter' in request.GET:
        search_filter = request.GET['search_filter']
        # print(search_filter)
        events = [{
            'id': x.id,
            'name': x.name,
            'category': x.categoryy,
            # 'firstImage': c.eventimage_set.first().image #Þarf að bæta við image model-i
        } for x in Event.objects.all().filter(name__icontains=search_filter)]
        events = list(Event.objects.filter(name__icontains=search_filter).values())
        # print(events)
        return JsonResponse({'data': events})
    context = {'events': Event.objects.all().order_by('name'), 'categories': Category.objects.all()}
    return render(request, 'events/indexx.html', context)


def get_event_by_id(request, id):
    list_of_similar_events = get_similar_events(id)
    return render(request, 'events/event_details.html', {
        'event': get_object_or_404(Event, pk=id), 'similar_events': list_of_similar_events})


def get_similar_events(id):
    this_event = Event.objects.get(id=id)
    category = this_event.categoryy
    return Event.objects.filter(categoryy=category).exclude(id=id)


def create_event(request):
    submitted = False
    if request.method == 'POST':
        form = EventCreateForm(request.POST)
        print(1)
        if form.is_valid():
            print(2)
            form.save()
            # event_img = EventImage(image=request.POST['image'], event=event)
            # event_img.save()
            return HttpResponseRedirect('/create_event?submitted=True')
    else:
        form = EventCreateForm()
        if 'submitted' in request.GET:
            submitted = True
        # TODO: Instance new EventCreateForm()
    return render(request, 'events/create_event.html', {
        'form': form})


def delete_event(request, id):
    event = get_object_or_404(Event, pk=id)
    event.delete()
    return redirect('event-index')


def checkbox_filter(request):
    selected_values = request.POST.getlist('category')
    return render(request, 'events/checkbox.html')


def checkout(request):
    context = {}
    return render(request, 'events/checkout.html', context)


@login_required
def boooking(request):
    submitted = False
    if request.method == 'POST':
        booking_form = EventBookingForm(data=request.POST)

        if booking_form.is_valid():
            booking_form.save()

            return HttpResponseRedirect('/booking?submitted=True')

    else:
        booking_form = EventBookingForm()
        if 'submitted' in request.GET:
            submitted = True
        # TODO: Instance new EventCreateForm()
    return render(request, 'events/booking.html', {
        'booking_form': booking_form})

# @login_required
# def user_profile(request):
#    return render(request, 'user_profile.html', {'user': request.user})
# redirectar á /accounts/profile
