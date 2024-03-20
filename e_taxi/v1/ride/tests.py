from django.test import TestCase
from rest_framework.test import APIClient
from  rest_framework import status

from v1.ride.models import ProjectUser, Driver, LocationCoordinates, Ride
from v1.ride.constants import UserTypes, RideStatus
from v1.ride.views import RideView
from v1.ride import serializers as ride_serlze


class RideModelTest(TestCase):

    def setUp(self):
        user = ProjectUser.objects.create_user(
            username='rider', email='rider@example.com', password='secret',
            user_type=UserTypes.USER)
        driver = Driver.objects.create_user(
            username='driver', email='driver@example.com', password='secret',
            user_type=UserTypes.DRIVER)
        pickup = LocationCoordinates.objects.create(
            latitude=10.853667, longitude=76.917792)
        destination = LocationCoordinates.objects.create(
            latitude=12.971599, longitude=77.594176)
        self.ride = Ride.objects.create(
            rider=user, pickup=pickup, destination=destination)

    def test_ride_creation(self):
        self.assertEqual(self.ride.status,
                         RideStatus.requested)
        self.assertIsNone(self.ride.driver)
        self.assertEqual(Driver.objects.get(
            username='driver').username, 'driver')

    def test_assign_driver(self):
        driver = Driver.objects.get(username='driver')
        self.ride.driver = driver
        self.ride.save()
        self.ride.refresh_from_db()

        self.assertEqual(self.ride.driver, driver)


class RideApiTest(TestCase):

    def setUp(self):
        self.client = APIClient()

        self.user = ProjectUser.objects.create_user(
            username="test_user", password="test_password")
        self.driver = Driver.objects.create_user(
            username="test_driver", password='password', user_type=102)

    def test_create_ride(self):
        ride_data = {
            "rider": self.user.pk,
            "pickup_coordinate": [1.343431, 2.345551],
            "destination_coordinate": [2.343431, 3.345551]
        }

        response = self.client.post("/ride/ride/", ride_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        created_ride = Ride.objects.get()
        serializer = ride_serlze.RideSerializer(created_ride)
        self.assertEqual(serializer.data, response.data)

        self.assertEqual(created_ride.rider, self.user)
        self.assertEqual(
            str(created_ride.pickup.latitude), str(ride_data['pickup_coordinate'][0]))
        self.assertEqual(
            str(created_ride.pickup.longitude), str(ride_data['pickup_coordinate'][1]))
        self.assertEqual(
            str(created_ride.destination.latitude), str(ride_data['destination_coordinate'][0]))
        self.assertEqual(
            str(created_ride.destination.longitude), str(ride_data['destination_coordinate'][1]))



