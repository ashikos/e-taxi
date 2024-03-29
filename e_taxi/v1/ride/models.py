from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from v1.ride.constants import UserTypes, RideStatus
from django.utils import timezone


# Create your models here.


class ProjectUser(AbstractUser):

    user_type = models.IntegerField(
        default=UserTypes.USER, choices=UserTypes.choices())

    class Meta:
        """Meta class for the above model."""

        verbose_name = ('ProjectUser')
        ordering = ('-id',)


class LocationCoordinates(models.Model):
    """Model to store location details
    Attirs:
        latitude(decimal): stores the geographical latitude
        longitude(decimal): stores the geographical longitude
        location(str): stores the name of location if available
        last_updated(datetime): store last updated time
    """
    latitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True,
                                   null=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True,
                                    null=True)
    location = models.CharField(max_length=100, null=True, blank=True,
                                default='')
    last_updated = models.DateTimeField(auto_now=True)

    def update_location(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude
        self.save()

    def __str__(self):
        return f'{self.pk} - {self.location} '


class Driver(ProjectUser):
    """Model to store details of driver
    Attirs:
        is_available(Bool): checks weather driver is available for ride or not
        coordinate(Fk): foreign key for coordinate
    """

    is_available = models.BooleanField(default=True)
    coordinate = models.ForeignKey(
        LocationCoordinates, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        """Meta class for the above model."""

        verbose_name = ('Driver')
        ordering = ('-id',)

    def __str__(self):
        return f'{self.user.username}'


class Ride(models.Model):
    """
    Model to store ride details of a ride
    Attirs:
        rider(Fk): foreign key to user store detail of customer
        driver(Fk): foreign key to user store detail of driver
        pickup(Fk): foreign key to coordinated stores pickup location
        destination(Fk): foreign key to coordinated stores delivery location
        status(Int): status of a ride
    """
    rider = models.ForeignKey(ProjectUser, related_name='rides_as_rider',
                              on_delete=models.CASCADE)
    driver = models.ForeignKey(Driver, related_name='rides_as_driver',
                               on_delete=models.CASCADE, null=True, blank=True)
    pickup = models.ForeignKey(
        LocationCoordinates, on_delete=models.SET_NULL, null=True, blank=True)
    destination = models.ForeignKey(
        LocationCoordinates, on_delete=models.SET_NULL, null=True, blank=True,
        related_name='rides')
    status = models.IntegerField(choices=RideStatus.choices(),
                              default=RideStatus.requested)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.pk} - {self.pickup.location} to {self.destination.location}'





