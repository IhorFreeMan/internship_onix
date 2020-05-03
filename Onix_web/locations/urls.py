# -*- coding: utf-8 -*-
from django.urls import path
from locations import views

urlpatterns = [
    path("", views.country_directory, name='country_directory'),
    path('country_detail=<int:id_city>', views.country_detail, name='country_detail'),
    path('city_detail=<int:id>', views.city_detail, name='city_detail'),
    path('delete_city=<int:id>', views.delete_city, name='delete_city'),
]




