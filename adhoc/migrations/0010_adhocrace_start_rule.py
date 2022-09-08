# Generated by Django 4.1 on 2022-08-27 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adhoc', '0009_adhocrace_index_delete_adhocracequeue'),
    ]

    operations = [
        migrations.AddField(
            model_name='adhocrace',
            name='start_rule',
            field=models.IntegerField(choices=[(0, 'cars locked until start'), (1, 'teleport false starters to pits'), (2, 'false starters must do a pit drivethru')], default=0),
        ),
    ]
