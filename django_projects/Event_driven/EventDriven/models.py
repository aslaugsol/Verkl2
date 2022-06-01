from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Event(models.Model):
    name = models.CharField(max_length=255)
    start_date = models.DateTimeField(default="2100-01-01 23:59:58")
    end_date = models.DateTimeField(default="2100-01-01 23:59:59")
    description = models.CharField(max_length=999, blank=True)
    categoryy = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True)
    price = models.FloatField()
    max_tickets = models.IntegerField()
    tickets_available = models.IntegerField()
    image = models.CharField(max_length=9999, default='')
    location = models.CharField(max_length=255, default='Unknown')


    def __str__(self):
        return self.name


class EventImage(models.Model):
    image = models.CharField(max_length=999)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)


class Admin(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Address(models.Model):
    zip = models.IntegerField()
    city = models.CharField(max_length=255)


class Tickets(models.Model):
    event_id = models.ForeignKey(Event, on_delete=models.CASCADE)
    name_on_ticket = models.ForeignKey(User, on_delete=models.CASCADE)


class Cart(models.Model):
    event_id = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_tickets = models.IntegerField(
        default=1,
        validators=[
            MaxValueValidator(10),
            MinValueValidator(1)
        ]
     )


class Credentials(models.Model):
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)


class PaymentInfo(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=255)
    card_number = models.CharField(max_length=255)


class Booking(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    complete = models.BooleanField(default=False, null=True, blank=False)
    transaction_id = models.CharField(max_length=200, null=True)

    def __str__(self):
        return str(self.id)

    @property
    def get_events(self):
        event = self.bookingitem_set.all()
        total = sum(item.quantity for item in event)
        return total


class BookingItem(models.Model):
    event = models.ForeignKey(Event, on_delete=models.SET_NULL, blank=True, null=True)
    booking = models.ForeignKey(Booking, on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField(
        default=0,
        validators=[
            MaxValueValidator(10),
            MinValueValidator(0)
        ]
     )
    @property
    def get_total(self):
        total = self.event.price * self.quantity
        return total



