# Generated by Django 3.1.4 on 2021-06-08 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracks', '0003_track_layout'),
    ]

    operations = [
        migrations.AddField(
            model_name='track',
            name='free_slots',
            field=models.IntegerField(default=1),
        ),
    ]
