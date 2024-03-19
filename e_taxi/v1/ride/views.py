import datetime
import jwt

from django.shortcuts import render
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from v1.ride import serializers as ride_serializer
from rest_framework import viewsets
from v1.ride import models as ride_models
from v1.ride import filters as ride_filter


# Create your views here.

class Signup(APIView):

    def post(self, request):
        serializer = ride_serializer.UserSerializer(data=request.data)
        serializer.is_valid()
        serializer.save()
        return Response(serializer.data)


class LoginView(APIView):

    def post(self, request):
        username = request.data['username']
        password = request.data['password']
        user = authenticate(username=username, password=password)
        if not user:
            raise AuthenticationFailed("username or password incorrect")

        payload = {
            "id": user.id,
            "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            "iat": datetime.datetime.utcnow()
        }

        token = jwt.encode(payload, "secret", algorithm="HS256")
        response = Response()

        response.set_cookie(key="jwt", value=token, httponly=True)
        response.data = {
            "jwt": token
        }

        return response


class UserView(APIView):
    """View to retrive user details"""
    # permission_classes = (permissions.IsAuthenticated, )

    def get(self, request, *args, **kwargs):

        user = request.user

        return Response(ride_serializer.UserSerializer(user).data)


class LogoutView(APIView):
    """View to logout and clear cookies"""
    def post(self, request):
        response = Response()
        response.delete_cookie(key="jwt")

        response.data = {
            "message": "succceessfully logged out"
        }

        return response


class RideView(viewsets.ModelViewSet):
    """views for ride"""

    queryset = ride_models.Ride.objects.all()
    serializer_class = ride_serializer.RideSerializer
    filterset_class = ride_filter.RideFilter


class DriverView(viewsets.ModelViewSet):
    """views for Driver"""

    queryset = ride_models.Driver.objects.all()
    serializer_class = ride_serializer.DriverSerializer


class LocationView(viewsets.ModelViewSet):
    """views for location"""

    queryset = ride_models.RideLocation.objects.all()
    serializer_class = ride_serializer.LocationSerializer
