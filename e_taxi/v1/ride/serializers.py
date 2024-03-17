from rest_framework import serializers
from v1.ride import models as ride_models
from rest_framework.exceptions import APIException


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


class RideSerializer(serializers.ModelSerializer):

    class Meta:
        model = ride_models.Ride
        fields = "__all__"


class LocationSerializer(serializers.ModelSerializer):

    class Meta:
        model = ride_models.RideLocation
        fields = "__all__"

