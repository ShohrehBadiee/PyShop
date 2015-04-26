from django.db import models

# Create your models here.



class Product(models.Model):
    name = models.CharField("Name", max_length=255)
    description = models.TextField("Description")
    price = models.FloatField("Price")
    created_at = models.DateField("Created at")
    updated_at = models.DateField("Updated at")
    quantity = models.IntegerField("Quantity")


class Picture(models.Model):
    product = models.ForeignKey(Product)
    picture = models.ImageField("Picture")
    description = models.TextField("Description")

