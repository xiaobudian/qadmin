# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qadmin', '0003_question'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='question',
            table='question',
        ),
    ]
