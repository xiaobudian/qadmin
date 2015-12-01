# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('qadmin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question_Answers',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('answer', models.TextField()),
                ('votes', models.IntegerField()),
                ('ct', models.DateTimeField(auto_now=True)),
                ('question_id', models.ForeignKey(to='qadmin.Question')),
                ('uid', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'question_answers',
            },
        ),
    ]
