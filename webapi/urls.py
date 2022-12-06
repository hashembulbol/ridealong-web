"""ridealong URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, register_converter
from webapi.views import *
from . import converts

register_converter(converts.FloatUrlParameterConverter, 'float')

urlpatterns = [
    path('login/', LoginView.as_view()),
    path('signup/', SignupView.as_view()),
    path('user/<str:username>/', UserView.as_view()),
    path('review/', ReviewView.as_view()),
    path('postreview/<str:username>/<str:author>/<str:content>/<int:stars>', PostReviewView.as_view()),
    path('trip/', TripView.as_view()),
    path('trip/create/<str:driver>/<float:originlat>/<float:originlon>/<float:destlat>/<float:destlon>/<int:capacity>/<str:date>/<str:time>/', CreateTripView.as_view()),
    path('trip/edit/<int:tripid>/<str:driver>/<float:originlat>/<float:originlon>/<float:destlat>/<float:destlon>/<int:capacity>/<str:date>/<str:time>/', EditTripView.as_view()),
    path('trip/leave/<str:username>/<int:id>/', TripLeaveView.as_view()),
    path('trip/join/<str:username>/<int:id>/<float:originlat>/<float:originlon>/<float:destlat>/<float:destlon>/<float:costinput>/<float:distance>/<int:seats>/', TripJoinView.as_view()),
    path('trip/status/<int:id>/<int:setstatus>/', TripStatusView.as_view())


]
