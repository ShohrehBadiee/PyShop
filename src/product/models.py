from django.db import models
from customer.models import Customer
from shop.models import Product


class ShoppingStatus(models.Model):
    status = models.CharField("Shopping Status", max_length=128)


class ShoppingCart(models.Model):
    customer = models.ForeignKey(Customer)
    status = models.ForeignKey(ShoppingStatus)
    total_price = models.FloatField("Total Price")
    created_at = models.DateField("Created at")
    updated_at = models.DateField("Updated at")


class Order(models.Model):
    card = models.ForeignKey(ShoppingCart)
    product = models.ForeignKey(Product)
    quantity = models.IntegerField("Count")
    unit_price = models.FloatField("Unit Price")


class PaymentMethod(models.Model):
    method = models.CharField("Payment Method", max_length=128)


class Payment(models.Model):
    customer = models.ForeignKey(Customer)
    card = models.ForeignKey(ShoppingCart)
    receipt_number = models.IntegerField()
    payment_method = models.ForeignKey(PaymentMethod)
    payment_date = models.DateField("Payment Date")
    confirm = models.BooleanField("Confirmed", default=False)







