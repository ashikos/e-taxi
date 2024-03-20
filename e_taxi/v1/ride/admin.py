# Register your models here.
from django.contrib import admin
from v1.ride.models import *


# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', "last_name", "user_type")


class RideAdmin(admin.ModelAdmin):
    list_display = ('rider', 'driver', "destination", "status")
    

class CoordinateAdmin(admin.ModelAdmin):
    list_display = ('location', 'latitude', 'longitude')


class DriverAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'is_available')


admin.site.register(ProjectUser, UserAdmin)
admin.site.register(Ride, RideAdmin)
admin.site.register(LocationCoordinates, CoordinateAdmin)
admin.site.register(Driver, DriverAdmin)
