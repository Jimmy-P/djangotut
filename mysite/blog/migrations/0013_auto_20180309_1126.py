# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_post_editor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='editor',
            field=models.ForeignKey(related_name='edits', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
