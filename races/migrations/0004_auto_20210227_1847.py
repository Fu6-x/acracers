# Generated by Django 3.1.4 on 2021-02-27 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('races', '0003_auto_20210216_0810'),
    ]

    operations = [
        migrations.AlterField(
            model_name='race',
            name='start_ts',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
