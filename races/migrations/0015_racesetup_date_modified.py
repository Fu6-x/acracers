# Generated by Django 4.1 on 2022-09-01 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('races', '0014_alter_racesetup_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='racesetup',
            name='date_modified',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
