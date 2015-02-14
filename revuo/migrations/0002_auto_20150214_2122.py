# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('revuo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogitem',
            name='deleted',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='newsitem',
            name='deleted',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='publication',
            name='deleted',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
