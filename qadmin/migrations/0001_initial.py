# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('nickname', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('pwd', models.CharField(max_length=35)),
                ('pic', models.CharField(max_length=100)),
                ('ct', models.DateTimeField(auto_now=True)),
                ('llt', models.DateTimeField()),
                ('status', models.IntegerField()),
            ],
        ),
    ]
