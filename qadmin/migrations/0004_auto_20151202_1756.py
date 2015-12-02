# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('qadmin', '0003_auto_20151201_1722'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('answer', models.TextField()),
                ('votes', models.IntegerField()),
                ('ct', models.DateTimeField(auto_now=True)),
                ('question', models.ForeignKey(to='qadmin.Question')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'answer',
            },
        ),
        migrations.RemoveField(
            model_name='question_answers',
            name='question',
        ),
        migrations.RemoveField(
            model_name='question_answers',
            name='user',
        ),
        migrations.DeleteModel(
            name='Question_Answers',
        ),
    ]
