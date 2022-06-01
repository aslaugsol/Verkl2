from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from EventDriven.forms.event_form import EventCreateForm, EventUpdateForm
from EventDriven.models import Event, Category, Booking, BookingItem, Customer
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
    submitted = False;
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


def update_event(request, id):
    instance = get_object_or_404(Event, pk=id)
    if request == 'POST':
        form = EventUpdateForm(data=request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect(request, 'event-details', id=id)
    else:
        form = EventUpdateForm(instance=instance)
        print(2)
    return render(request, 'events/update_event.html', {
        'form': form,
        'id': id})


def checkbox_filter(request):
    selected_values = request.POST.getlist('category')
    return render(request, 'events/checkbox.html', {})


def booking(request):
    if request.user.is_authenticated:
        customer = request.user
        booking_, created = Booking.objects.get_or_create(customer=customer, complete=False)
        event = booking_.bookingitem_set.all()
        bookingitem = booking_.get_events
    else:
        event = ['']
        booking_ = {'get_total':0, 'get_events':0}
        bookingitem = booking_['get_events']

    context = {'event': event, 'booking': booking_, 'bookingItem': bookingitem}

    return render(request, 'events/booking.html', context)


def checkout(request):
    context = {}
    return render(request, 'events/checkout.html', context)

def booking_selected(request):
    data = json.load(request.data)
    event_id = data['eventID']
    action = data['action']
    print('Action: ', action)
    print('EventId: ', event_id)

    customer = request.user.id
    event = Event.objects.get(id=event_id)
    booking_, created = Booking.objects.get_or_create(user=customer, complete=False)

    bookingit, created = BookingItem.objects.get_or_create(booking=booking_, event=event)

    if action == 'add':
        bookingit.quantity = (bookingit.quantity + 1)
    bookingit.save()


    return JsonResponse('Booking selected', safe=False)
# @login_required
# def user_profile(request):
#    return render(request, 'user_profile.html', {'user': request.user})
# redirectar á /accounts/profile
