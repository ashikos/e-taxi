# Generated by Django 4.2.6 on 2024-03-20 08:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ride', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='driver',
            options={'ordering': ('-id',), 'verbose_name': 'Driver'},
        ),
        migrations.AlterModelOptions(
            name='projectuser',
            options={'ordering': ('-id',), 'verbose_name': 'ProjectUser'},
        ),
        migrations.DeleteModel(
            name='RideLocation',
        ),
    ]
