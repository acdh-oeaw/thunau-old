# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-27 11:29
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='document',
            old_name='media',
            new_name='medium',
        ),
    ]