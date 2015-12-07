# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('qadmin', '0005_auto_20151204_1038'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='ct',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 7, 3, 4, 36, 407000, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
    ]
