# Generated by Django 5.1.6 on 2025-03-20 13:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0008_alter_project_start_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2025, 3, 20, 16, 50, 38, 720671), verbose_name='زمان شروع'),
        ),
    ]
