from django.db import models
from django.contrib.auth.models import User
from EventDriven.models import Category
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, default='Name')
    favorite_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    profile_photo = models.CharField(max_length=9999, default="https://cdn-icons-png.flaticon.com/512/149/149071.png")