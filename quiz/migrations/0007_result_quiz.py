# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-03 00:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0006_answer_question'),
    ]

    operations = [
        migrations.AddField(
            model_name='result',
            name='quiz',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='quiz.Quiz'),
            preserve_default=False,
        ),
    ]
