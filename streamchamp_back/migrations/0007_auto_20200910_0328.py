# Generated by Django 3.1.1 on 2020-09-10 03:28

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('streamchamp_back', '0006_auto_20200910_0326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='favorites',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), default=list, size=None),
        ),
    ]
