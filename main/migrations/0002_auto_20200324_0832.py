# Generated by Django 3.0.4 on 2020-03-24 08:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorial',
            name='tutorial_published',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 24, 8, 32, 8, 859048), verbose_name='date published'),
        ),
    ]
