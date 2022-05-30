from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from Event_driven import settings


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Event(models.Model):
    name = models.CharField(max_length=255)
    #start_date = models.DateTimeField()
    #end_date = models.DateTimeField()
    description = models.CharField(max_length=999, blank=True)
    categoryy = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True)
    price = models.FloatField()
    max_tickets = models.IntegerField()
    tickets_available = models.IntegerField()

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
    quantity = models.IntegerField(null=False,blank=False, validators=[
            MaxValueValidator(10),
            MinValueValidator(1)
        ])
    total_price = models.FloatField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

class Credentials(models.Model):
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

class PaymentInfo(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=255)
    card_number = models.CharField(max_length=255)
