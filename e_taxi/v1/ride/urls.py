from rest_framework.routers import SimpleRouter

from django.urls import path
from v1.ride import views
from v1.ride.models import *


router = SimpleRouter()


router.register(r'ride', views.RideView, basename=Ride)
router.register(r'driver', views.DriverView, basename=Ride)


urlpatterns = [
    path('signup/', views.Signup .as_view()),
    path('login/', views.LoginView .as_view()),
    path('user/', views.UserView .as_view()),
    path('logout/', views.LogoutView .as_view()),

]

urlpatterns += router.urls