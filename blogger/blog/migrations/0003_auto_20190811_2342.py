# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2019-08-11 18:12
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_blogcomment'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='BlogComment',
            new_name='Comments',
        ),
    ]