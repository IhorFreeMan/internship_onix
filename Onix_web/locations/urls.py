# -*- coding: utf-8 -*-
from django.urls import path
from locations import views

app_name = 'locations'

urlpatterns = [
    path('', views.country_directory, name='country_directory'),
    path('country_detail=<int:id_city>', views.country_detail, name='country_detail'),
    path('city_detail=<int:id>', views.city_detail, name='city_detail'),
    path('delete_city=<int:id>', views.delete_city, name='delete_city'),
    path('add_country/', views.add_country, name='add_country'),
    path('edit_country=<int:id>', views.edit_country, name='edit_country'),
    path('add_city/', views.add_city, name='add_city'),
    path('edit_city=<int:id>', views.edit_city, name='edit_city'),
]




