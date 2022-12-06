
from dataclasses import fields
import profile
from turtle import update
from urllib.request import Request
from rest_framework import serializers
from .models import Review, User, Trip
from django.contrib.auth.hashers import make_password

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = '__all__'
        depth = 1

    def create(self, validated_data):

        user = User.objects.create(
        username=validated_data['username'],
        password = make_password(validated_data['password']),
        is_driver = validated_data['is_driver']
        )
        return user
    
    def update(self, instance, validated_data):
        password = make_password(validated_data['password'])
        validated_data['password'] = password
        return super().update(instance, validated_data)

class TripSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trip
        fields = '__all__'
        depth = 1

class ReviewSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Review
        fields = '__all__'
        depth = 1





    
