from django.db import models

# Create your models here.


class Event(models.Model):
    name = models.CharField(max_length=255)
    date = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    price = models.FloatField()
    max_tickets = models.IntegerField()
    tickets_available = models.IntegerField()

    def __str__(self):
        return self.name

class User(models.Model):
    name = models.CharField(max_length=255)
    favorites = models.CharField(max_length=255)
    profile_photo = models.CharField(max_length=9999)

    def __str__(self):
        return self.name

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
