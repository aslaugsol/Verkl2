from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Event(models.Model):
    name = models.CharField(max_length=255)
    date = models.DateField()
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

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    profile_photo = models.CharField(max_length=255)


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
    event_name = models.CharField(max_length=255)
    total_price = models.FloatField()

class Credentials(models.Model):
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

class PaymentInfo(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=255)
    card_number = models.CharField(max_length=255)
