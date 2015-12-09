# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qadmin', '0009_auto_20151209_1417'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='aboutme',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
