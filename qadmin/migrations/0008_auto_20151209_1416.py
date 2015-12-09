# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qadmin', '0007_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='aboutme',
            field=models.CharField(max_length=500, blank=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='birthday',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='location',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='realname',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
