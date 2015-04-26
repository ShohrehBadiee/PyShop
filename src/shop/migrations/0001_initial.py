# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('picture', models.ImageField(upload_to=b'', verbose_name=b'Picture')),
                ('description', models.TextField(verbose_name=b'Description')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name=b'Name')),
                ('description', models.TextField(verbose_name=b'Description')),
                ('price', models.FloatField(verbose_name=b'Price')),
                ('created_at', models.DateField(verbose_name=b'Created at')),
                ('updated_at', models.DateField(verbose_name=b'Updated at')),
                ('quantity', models.IntegerField(verbose_name=b'Quantity')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='picture',
            name='product',
            field=models.ForeignKey(to='shop.Product'),
            preserve_default=True,
        ),
    ]
