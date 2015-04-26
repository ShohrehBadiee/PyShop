from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Customer(User):
    address = models.TextField("Address")
    phone = models.CharField("Phone", max_length=15)
    is_staff = False
