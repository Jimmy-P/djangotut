# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20180305_0959'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='edited',
            field=models.DateTimeField(default=datetime.datetime(2018, 3, 7, 12, 37, 2, 494017, tzinfo=utc), blank=True),
            preserve_default=False,
        ),
    ]
