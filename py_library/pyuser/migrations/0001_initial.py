# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-27 08:47
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PyUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unionId', models.CharField(max_length=100, unique=True)),
                ('nickName', models.CharField(max_length=100)),
                ('avatarUrl', models.CharField(max_length=256)),
                ('type', models.IntegerField(blank=True, choices=[(0, 'user just can browser the info'), (1, 'user can borrow and return book'), (2, 'py library administrator')], default=0)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
