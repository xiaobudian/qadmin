# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qadmin', '0008_auto_20151209_1416'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='description',
            field=models.TextField(null=True),
        ),
    ]
