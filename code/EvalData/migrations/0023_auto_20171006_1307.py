# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-10-06 20:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('EvalData', '0022_auto_20171005_1858'),
    ]

    operations = [
        migrations.AlterField(
            model_name='directassessmentresult',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='evaldata_directassessmentresult_items', related_query_name='evaldata_directassessmentresult_item', to='EvalData.TextPair', verbose_name='Item'),
        ),
        migrations.AlterField(
            model_name='directassessmentresult',
            name='task',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='evaldata_directassessmentresult_tasks', related_query_name='evaldata_directassessmentresult_task', to='EvalData.DirectAssessmentTask', verbose_name='Task'),
        ),
    ]