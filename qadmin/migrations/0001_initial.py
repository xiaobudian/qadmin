# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=150)),
                ('content', models.TextField()),
                ('ct', models.DateTimeField(auto_now=True)),
                ('votes', models.IntegerField()),
                ('answers', models.IntegerField()),
                ('views', models.IntegerField()),
            ],
            options={
                'db_table': 'question',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('description', models.TextField()),
                ('uid', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'tag',
            },
        ),
        migrations.AddField(
            model_name='question',
            name='tags',
            field=models.ManyToManyField(to='qadmin.Tag'),
        ),
        migrations.AddField(
            model_name='question',
            name='uid',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
