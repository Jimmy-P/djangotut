# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_auto_20180312_1253'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='whosviewed',
            field=jsonfield.fields.JSONField(default='null'),
            preserve_default=False,
        ),
    ]
