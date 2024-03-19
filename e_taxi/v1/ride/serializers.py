from rest_framework import exceptions
from rest_framework import serializers
from v1.ride import models as ride_models
from rest_framework.exceptions import APIException

from v1.ride import utils


class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=False)

    class Meta:
        """Meta info"""
        model = ride_models.ProjectUser
        fields = "__all__"

    def create(self, validated_data):
        """overide create to create user"""
        email = validated_data['email']
        if ride_models.ProjectUser.objects.filter(username=email).exists():
            raise APIException("Email already existings")
        validated_data["username"] = email
        password = validated_data.pop('password')
        user = super().create(validated_data)
        user.set_password(password)
        user.save()
        return user


class DriverSerializer(serializers.ModelSerializer):
    user_details = serializers.SerializerMethodField(required=False)

    class Meta:
        model = ride_models.Driver
        fields = "__all__"

    def get_user_details(self, instance):
        data = {
            "first_name": instance.user.first_name,
            "last_name": instance.user.last_name
        }
        return data

    def create(self, validated_data):
        """overide create to create user"""

        if "user" not in validated_data.keys():
            raise exceptions.NotFound("User Not Found")
        user = super().create(validated_data)
        return user


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ride_models.RideLocation
        fields = "__all__"

    # def update(self, instance, validated_data):


class LocationCoordinatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ride_models.LocationCoordinates
        fields = "__all__"


class RideSerializer(serializers.ModelSerializer):
    pickup_coordinate = serializers.ListField(
        child=serializers.DecimalField(max_digits=9, decimal_places=6),
        write_only=True
    )
    destination_coordinate = serializers.ListField(
        child=serializers.DecimalField(max_digits=9, decimal_places=6),
        write_only=True
    )
    pickup_location = serializers.CharField(write_only=True, required=False)
    destination_loc = serializers.CharField(write_only=True, required=False)

    # method fields
    location = serializers.SerializerMethodField(required=False)

    class Meta:
        model = ride_models.Ride
        exclude = ['pickup', 'destination']

    def get_location(self, instance):

        lat1 = instance.pickup.latitude
        lon1 = instance.pickup.longitude
        lat2 = instance.destination.latitude
        lon2 = instance.destination.longitude

        distance = utils.haversine_distance(lat1, lon1, lat2, lon2)

        data = {
            'pickup_coordinate': [lat1, lon1],
            'pickup_location': instance.pickup.location,
            'destination_coordinate': [lat2, lon2],
            'destination_loc': instance.destination.location,
            'distance': f'{distance} km'
        }
        return data

    def create(self, validated_data):
        """overide create to create Ride"""

        if 'pickup_coordinate' not in validated_data.keys():
            raise exceptions.NotFound("Pickup Location Not Found")

        if 'destination_coordinate' not in validated_data.keys():
            raise exceptions.NotFound("Destination Not Found")

        pickup_coordinate = validated_data.pop('pickup_coordinate')
        pickup_location = validated_data.pop('pickup_location')
        destination_coordinate = validated_data.pop('destination_coordinate')
        destination = validated_data.pop('destination_loc')

        pickup_data = {
            'latitude': pickup_coordinate[0],
            'longitude': pickup_coordinate[1],
            'location': pickup_location
        }
        pickup = ride_models.LocationCoordinates.objects.create(**pickup_data)

        destination_data = {
            'latitude': destination_coordinate[0],
            'longitude': destination_coordinate[1],
            'location': destination
        }
        destination = ride_models.LocationCoordinates.objects.create(
            **destination_data)

        validated_data['pickup'] = pickup
        validated_data['destination'] = destination

        ride = super().create(validated_data)
        return ride

    def update(self, instance, validated_data):

        # if validated_data

        ride = super().update(instance, validated_data)
        return ride
