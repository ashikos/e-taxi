from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser, Group, Permission
from v1.ride.constants import UserTypes, RideStatus
from django.utils import timezone


# Create your models here.


class ProjectUser(AbstractUser):
    user_type = models.IntegerField(
        default=UserTypes.USER, choices=UserTypes.choices())


class Ride(models.Model):
    rider = models.ForeignKey(ProjectUser, related_name='rides_as_rider',
                              on_delete=models.CASCADE)
    driver = models.ForeignKey(ProjectUser, related_name='rides_as_driver',
                               on_delete=models.CASCADE)
    pickup_location = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=RideStatus.choices(),
                              default=RideStatus.requested)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.pk} - {self.rider.username} to {self.dropoff_location}'


class RideLocation(models.Model):
    ride = models.OneToOneField(
        Ride, on_delete=models.CASCADE, related_name='location')
    latitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True,
                                   null=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True,
                                    null=True)
    last_updated = models.DateTimeField(auto_now=True)

    def update_location(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude
        self.save()

    def __str__(self):
        return f'{self.pk} - {self.ride.destination}'
