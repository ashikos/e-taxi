# Register your models here.
from django.contrib import admin
from v1.ride.models import *


# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', "last_name", "user_type")


class RideAdmin(admin.ModelAdmin):
    list_display = ('rider', 'driver', "destination", "status")


class LocationAdmin(admin.ModelAdmin):
    list_display = ('ride', 'latitude', "longitude", "last_updated")


admin.site.register(Ride, RideAdmin)
admin.site.register(RideLocation, LocationAdmin)
admin.site.register(ProjectUser, UserAdmin)
