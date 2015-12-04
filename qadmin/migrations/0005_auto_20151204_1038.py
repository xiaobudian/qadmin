# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qadmin', '0004_auto_20151202_1756'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='reputation',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='answer',
            name='votes',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='question',
            name='answers',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='question',
            name='views',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='question',
            name='votes',
            field=models.IntegerField(default=0),
        ),
    ]
