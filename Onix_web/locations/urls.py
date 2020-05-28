# -*- coding: utf-8 -*-
from django.urls import path
from locations import views

app_name = 'locations'

urlpatterns = [
    path('', views.country_directory, name='country_directory'),
    path('country/<int:id_city>/detail', views.country_detail, name='country_detail'),
    path('city/<int:id>/detail', views.city_detail, name='city_detail'),
    path('city/<int:id>/delete', views.delete_city, name='delete_city'),
    path('add_country/', views.add_country, name='add_country'),
    path('country/<int:id>/edit', views.edit_country, name='edit_country'),
    path('add_city/', views.add_city, name='add_city'),
    path('city/<int:id>/edit', views.edit_city, name='edit_city'),
]




