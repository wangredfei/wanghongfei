# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-01-16 11:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0007_book_publisher'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='author_set',
            field=models.ManyToManyField(to='index.Author'),
        ),
    ]
