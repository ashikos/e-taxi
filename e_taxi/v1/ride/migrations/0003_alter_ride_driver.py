# Generated by Django 4.2.6 on 2024-03-19 05:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ride', '0002_rename_pickup_coordinate_ride_pickup_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ride',
            name='driver',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rides_as_driver', to='ride.driver'),
        ),
    ]
