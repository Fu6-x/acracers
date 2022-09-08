# Generated by Django 4.1 on 2022-08-23 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='props',
            name='admin_password',
            field=models.CharField(blank=True, default='', max_length=15),
        ),
        migrations.AddField(
            model_name='props',
            name='fixed_setups',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='props',
            name='join_password',
            field=models.CharField(blank=True, default='', max_length=15),
        ),
        migrations.AddField(
            model_name='props',
            name='practice_minutes',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='props',
            name='qualifying_minutes',
            field=models.IntegerField(blank=True, default=10, null=True),
        ),
        migrations.AddField(
            model_name='props',
            name='race_minutes',
            field=models.IntegerField(blank=True, default=15, null=True),
        ),
        migrations.AddField(
            model_name='props',
            name='reverse_grid',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='props',
            name='show_public',
            field=models.BooleanField(default=False),
        ),
    ]
