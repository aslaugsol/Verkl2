from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from EventDriven.forms.event_form import EventCreateForm, EventBookingForm, BookingCheckoutForm, AddressCheckoutForm
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
        events = list(events.filter(name__icontains=search_filter).values())
        # print(events)
        return JsonResponse({'data': events})
    #if request.method == 'GET':
        #print('Inn if')
        #category_id = request.GET['dataCategory']
        #print(category_id)
        #sel_category_events = category_events(category_id)
        #return JsonResponse({'selected_category_events': sel_category_events})
    context = {'events': Event.objects.all().order_by('name'), 'categories': Category.objects.all()}
    return render(request, 'events/indexx.html', context)

def index2(request, string):
    Event.objects.filter(name__icontains=string)
    context = {}
    return render(request, 'events/indexx.html', context)


def category_events(category_id):
    print(category_id)
    all_events = Event.objects.all()
    if category_id == 0:
        return all_events
    else:
        selected_category_events = all_events.filter(categoryy=category_id)
        print(selected_category_events)
        return selected_category_events

def about_us(request):
    about_us_text = "EventDriven is a ticketing company in Iceland, we handle ticket sales for all types of events. EventDriven aims to keep your online ticketing as easy as it can be for all parties. Our employees are experts in ticketing and have set up ticket sales all over the world. Founders are Áslaug Sól Sigurðardóttir, Karítas Etna Elmarsdóttir, Sölvi Karl Einarsson.  They have a Bachelor degree in Engineering from the University of Reykjavík. The website was officially opened on June 3rd  and has been and will be under constant development to meet the needs of both ticket buyers and event promoters. For Event Promoters, please contact info@eventdriven.con for more information check out"
    return render(request, 'events/about_us.html', {'text': about_us_text})


def get_event_by_id(request, id):
    list_of_similar_events = get_similar_events(id)
    string = ""
    if len(list_of_similar_events) == 0:
        string += "There are no similar events"
    return render(request, 'events/event_details.html', {
        'event': get_object_or_404(Event, pk=id), 'similar_events': list_of_similar_events, 'no_events': string})


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


def checkbox_filter(request):
    selected_values = request.POST.getlist('category')
    return render(request, 'events/checkbox.html')


def checkout(request):
    submitted = False
    if request.method == 'POST':
        payment_form = BookingCheckoutForm(data=request.POST)

        if payment_form.is_valid():
            payment_form.save()

            return redirect('checkout_email/confirmation_email')

    else:
        payment_form = BookingCheckoutForm()
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'events/checkout.html', {
        'payment_form': payment_form})


def address_checkout(request):
    submitted = False
    if request.method == 'POST':
        payment_form = BookingCheckoutForm(data=request.POST)
        address_form = AddressCheckoutForm(data=request.POST)
        if payment_form.is_valid():
            payment_form.save()
            if address_form.is_valid():
                address_form.save()
                return redirect('checkout_address/confirmation_address')

    else:
        payment_form = BookingCheckoutForm()
        address_form = AddressCheckoutForm()
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'events/checkout_address.html', {
        'payment_form': payment_form, 'address_form': address_form})

def confirmation_email(request):
    context = {'Confirmation': ""}
    return render(request, 'events/confirmation_email.html', context)

def confirmation_address(request):
    context = {'Confirmation': ""}
    return render(request, 'events/confirmation_address.html', context)

def eventFilter(request, id, schedule=None):
    latest_schedule_update = schedule.objects.all()
    context = {'latest_schedule_update': json.dumps(latest_schedule_update)}
    return render(request, 'sessionscheduler.html', context)


@login_required
def boooking(request):
    submitted = False
    if request.method == 'POST':
        booking_form = EventBookingForm(data=request.POST)

        if booking_form.is_valid():
            booking_form.save()
            data = booking_form.cleaned_data
            choice = data['delivery']
            if 'postal' in str(choice):
                return redirect('/checkout_address')
            else:
                return redirect('/checkout')

    else:
        booking_form = EventBookingForm()
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'events/booking.html', {
        'booking_form': booking_form})

# @login_required
# def user_profile(request):
#    return render(request, 'user_profile.html', {'user': request.user})
# redirectar á /accounts/profile
