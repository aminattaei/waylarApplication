# Generated by Django 5.1.6 on 2025-03-23 10:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0015_projectengineer_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectengineer',
            name='post',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='projects.project'),
        ),
    ]
