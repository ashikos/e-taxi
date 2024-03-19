from django_filters import rest_framework as filters
from v1.ride.models import *
from django.db.models import Q


class RideFilter(filters.FilterSet):
    """filtering Entries"""
    status = filters.CharFilter(method='status_filter')
    date = filters.CharFilter(method='date_filter')

    class Meta:
        """Meta info"""
        model = Ride
        fields = "__all__"

    def status_filter(self, queryset, name, value):

        queryset = queryset.filter(status=value)

        return queryset