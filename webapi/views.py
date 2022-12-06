from email.policy import HTTP
from re import T
from turtle import st
from unicodedata import decimal
from webbrowser import get
from django.shortcuts import render
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from decimal import Decimal

from webapi.models import Point, Review, Ride, TripStatus, User, Trip
from webapi.serializers import ReviewSerializer, TripSerializer, UserSerializer
# Create your views here.


class LoginView(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
  
    def get(self, request, format=None):
        
        serializer = UserSerializer(User.objects.get(username= request.user))
        return Response(serializer.data, status.HTTP_200_OK)

class SignupView(APIView):

    def post(self, request):

        serializer = UserSerializer(data=request.data) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

class UserView(APIView):
     def get_object(self, username):
        try:
            return User.objects.get(username=username)
        except User.DoesNotExist:
            return Response(status.HTTP_404_NOT_FOUND)

     def put(self, request, username):
        serializer = UserSerializer(self.get_object(username), data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
    
     def get(self, request, username):
        serializer = UserSerializer(self.get_object(username))
        return Response(serializer.data)

        

class TripView(APIView):
     def post(self, request):
        serializer = TripSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

     def get(self, request):
        serializer = TripSerializer(Trip.objects.all(), many=True)
        return Response(serializer.data)
     
class CreateTripView(APIView):
    def get_user(self, username):
        try:
            return User.objects.get(username=username)
        except User.DoesNotExist:
            return Response(status.HTTP_404_NOT_FOUND)
    
    def get(self, request, driver, originlat, originlon, destlat, destlon, capacity, date, time):
        d = self.get_user(driver)
        s = TripStatus.objects.get(id=2)
        origin = Point.objects.create(user=d, lat=originlat, lon=originlon, type=1)
        dest = Point.objects.create(user=d, lat=destlat, lon=destlon, type=2)
        trip = Trip.objects.create(driver=d, status=s,capacity=capacity, tripdate=date, triptime = time)
        trip.points.add(origin)
        trip.points.add(dest)
        trip.save()
        return Response(status.HTTP_200_OK)

class EditTripView(APIView):
    def get_user(self, username):
        try:
            return User.objects.get(username=username)
        except User.DoesNotExist:
            return Response(status.HTTP_404_NOT_FOUND)
    
    def get(self, request, tripid, driver, originlat, originlon, destlat, destlon, capacity, date, time):
        d = self.get_user(driver)

        origin = Point.objects.create(user=d, lat=originlat, lon=originlon, type=1)
        dest = Point.objects.create(user=d, lat=destlat, lon=destlon, type=2)


        trip = Trip.objects.get(id=tripid)

        trip.capacity = capacity
        trip.tripdate = date
        trip.triptime = time

        trip.points.clear()

        
        trip.points.add(origin)
        trip.points.add(dest)
        
        trip.save()
        
        return Response(status.HTTP_200_OK)

class TripJoinView(APIView):
     def get(self, request, username, id, originlat, originlon, destlat, destlon, costinput, distance, seats):
        
        user = User.objects.get(username=username)
        trip = Trip.objects.get(id=id)
        trip.passengers.add(user)
        
        p1 = Point.objects.create(user=user, lat=originlat, lon=originlon, type=1)
        p2 = Point.objects.create(user=user, lat=destlat, lon=destlon, type=2)

        trip.points.add(p1)
        trip.points.add(p2)

        ride = Ride.objects.create(user=user, cost=costinput, trip=trip, distance=distance, seats=seats)
        trip.rides.add(ride)

        trip.reserved += seats
        
        trip.revenue += Decimal(costinput)

        trip.save()

        return Response(status.HTTP_200_OK)
        
class TripLeaveView(APIView):
    def get(self, request, username, id):
        user = User.objects.get(username=username)
        trip = Trip.objects.get(id=id)
        trip.passengers.remove(user)
        points = Point.objects.filter(user=user.id)
        points.delete()

        ride = trip.rides.get(user=user.id)
        
        trip.reserved -= ride.seats
        trip.revenue -= Decimal(ride.cost)

        ride.delete()
        trip.save()

        return Response(status.HTTP_200_OK)

class TripStatusView(APIView):
    def get(self, request, id, setstatus):
        trip = Trip.objects.get(id=id)
        trip.status = TripStatus.objects.get(id=setstatus)
        trip.save()
        return Response(status.HTTP_200_OK)

class ReviewView(APIView):
     def get(self, request):
        serializer = ReviewSerializer(Review.objects.all(), many=True)
        return Response(serializer.data)

class PostReviewView(APIView):
    def get(self, request, username, author, content, stars):
        user = User.objects.get(username=username)
        author = User.objects.get(username=author)
        review = Review.objects.create(user=user,author= author, content=content, stars=stars)
        return Response(status= status.HTTP_201_CREATED)


