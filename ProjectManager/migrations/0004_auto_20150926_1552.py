# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ProjectManager', '0003_auto_20150907_1913'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actionplan',
            name='Date_Due',
            field=models.DateTimeField(verbose_name='due date'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='DateSeen',
            field=models.DateTimeField(verbose_name='date seen'),
        ),
    ]
