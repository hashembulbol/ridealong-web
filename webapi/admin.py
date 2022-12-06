from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from webapi.models import User,TripStatus, Trip ,Review, Point, Ride

# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(TripStatus)
admin.site.register(Trip)
admin.site.register(Review)
admin.site.register(Ride)
admin.site.register(Point)

