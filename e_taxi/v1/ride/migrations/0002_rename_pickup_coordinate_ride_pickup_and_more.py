# Generated by Django 4.2.6 on 2024-03-18 11:26

from django.db import migrations, models
import v1.ride.constants


class Migration(migrations.Migration):

    dependencies = [
        ('ride', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ride',
            old_name='pickup_coordinate',
            new_name='pickup',
        ),
        migrations.AlterField(
            model_name='ride',
            name='status',
            field=models.IntegerField(choices=[(101, 'requested'), (102, 'accepted'), (103, 'in progress'), (104, 'completed'), (105, 'cancelled')], default=v1.ride.constants.RideStatus['requested']),
        ),
    ]