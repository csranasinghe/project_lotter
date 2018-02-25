# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-25 17:34
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('lotter', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalproject',
            name='assignee',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='project',
            name='assignee',
            field=models.OneToOneField(blank=True, default='', on_delete=django.db.models.deletion.SET_DEFAULT, to=settings.AUTH_USER_MODEL),
        ),
    ]