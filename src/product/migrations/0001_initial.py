# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '__first__'),
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('quantity', models.IntegerField(verbose_name=b'Count')),
                ('unit_price', models.FloatField(verbose_name=b'Unit Price')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('receipt_number', models.IntegerField()),
                ('payment_date', models.DateField(verbose_name=b'Payment Date')),
                ('confirm', models.BooleanField(default=False, verbose_name=b'Confirmed')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PaymentMethod',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('method', models.CharField(max_length=128, verbose_name=b'Payment Method')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ShoppingCart',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('total_price', models.FloatField(verbose_name=b'Total Price')),
                ('created_at', models.DateField(verbose_name=b'Created at')),
                ('updated_at', models.DateField(verbose_name=b'Updated at')),
                ('customer', models.ForeignKey(to='customer.Customer')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ShoppingStatus',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.CharField(max_length=128, verbose_name=b'Shopping Status')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='shoppingcart',
            name='status',
            field=models.ForeignKey(to='product.ShoppingStatus'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='payment',
            name='card',
            field=models.ForeignKey(to='product.ShoppingCart'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='payment',
            name='customer',
            field=models.ForeignKey(to='customer.Customer'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='payment',
            name='payment_method',
            field=models.ForeignKey(to='product.PaymentMethod'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='order',
            name='card',
            field=models.ForeignKey(to='product.ShoppingCart'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='order',
            name='product',
            field=models.ForeignKey(to='shop.Product'),
            preserve_default=True,
        ),
    ]
