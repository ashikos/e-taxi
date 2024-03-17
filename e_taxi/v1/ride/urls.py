from rest_framework.routers import SimpleRouter

from django.urls import path
from v1.ride import views
from v1.ride.models import *


router = SimpleRouter()


router.register(r'bill', views.RideView, basename=Ride)


urlpatterns = [ ]

urlpatterns += router.urls