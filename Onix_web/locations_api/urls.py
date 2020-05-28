# -*- coding: utf-8 -*-
from django.urls import path, include
from locations_api import views
from rest_framework import routers


app_name = 'locations_api'

# generics
urlpatterns = [

    path('country-list/', views.CountryListView.as_view()),
    path('country-add/', views.CountryAddView.as_view()),
    path('country-details-<int:pk>/', views.CountryDetailView.as_view()),
]

# viewsets
router = routers.DefaultRouter()
router.register('city', views.CityAddView)
urlpatterns += [
    path('', include(router.urls)),
]