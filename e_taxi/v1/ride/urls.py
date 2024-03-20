from rest_framework.routers import SimpleRouter

from django.urls import path
from . import views
from v1.ride.models import *


router = SimpleRouter()


router.register(r'ride', views.RideView, basename=Ride)
router.register(r'driver', views.DriverView, basename=Ride)


urlpatterns = [
    path('signup/', views.Signup.as_view()),
    path('login/', views.LoginView.as_view()),
    path('user/', views.UserView.as_view()),
    path('logout/', views.LogoutView.as_view()),

    path('<int:pk>/accept/', views.RideAcceptView.as_view(
        {'patch': 'update'}), name='ride-accept'),

]

urlpatterns = urlpatterns + router.urls
