import jwt

from rest_framework import permissions
from rest_framework.exceptions import AuthenticationFailed
from rest_framework import exceptions
from v1.ride.models import ProjectUser
from v1.ride import constants as ride_consts


class IsDriver(permissions.BasePermission):

    def has_permission(self, request, view):

        token = request.COOKIES.get("jwt")
        if not token:
            raise exceptions.NotFound("Token Not Found")

        try:
            payload = jwt.decode(token, "secret", algorithms=["HS256"])
            user = ProjectUser.objects.get(id=payload['id'])
        except:
            raise AuthenticationFailed

        if not user.user_type == ride_consts.UserTypes.DRIVER:
            raise exceptions.AuthenticationFailed("Only drivers can accept")

        request.user = user
        # view.kwargs["user"] = user

        return True


class IsAuthenticated(permissions.BasePermission):

    def has_permission(self, request, view):

        token = request.COOKIES.get("jwt")
        if not token:
            raise exceptions.NotFound("Token Not Found")

        try:
            payload = jwt.decode(token, "secret", algorithms=["HS256"])
            user = ProjectUser.objects.get(id=payload['id'])
        except:
            raise AuthenticationFailed

        if not user.type == ride_consts.UserTypes.DRIVER:
            raise exceptions.AuthenticationFailed("Only drivers can accept")

        request.user = user
        view.kwargs["user"] = user

        return True
