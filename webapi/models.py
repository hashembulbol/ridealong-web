from ast import Pass
from datetime import datetime
from email.policy import default
from lib2to3.pgen2 import driver
from pyexpat import model
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    created_at = models.DateTimeField(auto_now_add=True)
    is_driver = models.BooleanField(default=False)
    mobile = models.CharField(max_length=15,null= True)
    car = models.CharField(max_length=30, null =True)
    kmprice = models.DecimalField(decimal_places=1, max_digits=2, default=0.7)


class TripStatus(models.Model):
    name = models.CharField(max_length=15)

class Point(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    address = models.TextField()
    lon = models.DecimalField(max_digits=9, decimal_places=7)
    lat = models.DecimalField(max_digits=9, decimal_places=7)
    place_id = models.CharField(max_length=30, default="" ,blank=True)
    type = models.IntegerField(default=1)

class Trip(models.Model):
    driver = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    passengers = models.ManyToManyField(User, related_name='+')
    capacity = models.IntegerField(default=1)
    reserved = models.IntegerField(default=0)
    status = models.ForeignKey(TripStatus, on_delete=models.CASCADE)
    tripdate = models.DateField(blank=True, null=True)
    triptime = models.TimeField(blank=True, null=True)
    distance = models.IntegerField(default=0)
    revenue = models.DecimalField(default=0, decimal_places=2, max_digits=5)
    created_at = models.DateTimeField(auto_now_add=True)
    points = models.ManyToManyField(Point)
    rides = models.ManyToManyField('Ride', related_name='rides')

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author')
    content = models.TextField()
    stars = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

class Ride(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cost = models.DecimalField(default=0, decimal_places=2, max_digits=5)
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
    distance = models.DecimalField(default=0, decimal_places=2, max_digits=5)
    seats = models.IntegerField(default=1)

