from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('add/', views.add_weather_data, name="Add_Weather")

]
