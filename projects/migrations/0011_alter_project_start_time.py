# Generated by Django 5.1.6 on 2025-03-21 13:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0010_alter_project_start_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2025, 3, 21, 17, 4, 33, 618948), verbose_name='زمان شروع'),
        ),
    ]
