# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qadmin', '0002_question_answers'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='uid',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='question_answers',
            old_name='question_id',
            new_name='question',
        ),
        migrations.RenameField(
            model_name='question_answers',
            old_name='uid',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='tag',
            old_name='uid',
            new_name='user',
        ),
    ]
