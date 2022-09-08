# Generated by Django 3.1.4 on 2021-06-01 11:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, unique=True)),
                ('slug', models.CharField(max_length=128, unique=True)),
                ('rsr_id', models.IntegerField(default=0)),
                ('dlc_slug', models.CharField(blank=True, default='', max_length=128)),
                ('download_url', models.URLField(blank=True, default='', max_length=2048)),
            ],
        ),
        migrations.CreateModel(
            name='Laptime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seconds', models.FloatField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cars.car')),
            ],
        ),
    ]
