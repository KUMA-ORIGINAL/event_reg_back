# Generated by Django 5.0 on 2024-10-04 18:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0003_remove_team_captain'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teamcaptain',
            name='team',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='captain', to='registration.team'),
        ),
    ]