# Generated by Django 4.0.6 on 2022-07-21 15:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('drivers', '0001_initial'),
        ('tracks', '0005_alter_track_slug_alter_track_title'),
        ('cars', '0004_auto_20220709_1240'),
    ]

    operations = [
        # migrations.AddField(
        #     model_name='laptime',
        #     name='best',
        #     field=models.FloatField(null=True),
        # ),
        # migrations.AddField(
        #     model_name='laptime',
        #     name='driver',
        #     field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='drivers.driver'),
        # ),
        # migrations.AddField(
        #     model_name='laptime',
        #     name='middle',
        #     field=models.FloatField(null=True),
        # ),
        # migrations.AddField(
        #     model_name='laptime',
        #     name='num_entries',
        #     field=models.IntegerField(null=True),
        # ),
        # migrations.AddField(
        #     model_name='laptime',
        #     name='track',
        #     field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='tracks.track'),
        # ),
        # migrations.AddField(
        #     model_name='laptime',
        #     name='worst',
        #     field=models.FloatField(null=True),
        # ),
        migrations.AlterField(
            model_name='laptime',
            name='seconds',
            field=models.FloatField(null=True),
        ),
    ]
