# -*- coding: utf-8 -*-
from django.urls import path, include
from locations_api import views
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


app_name = 'locations_api'


# generics
urlpatterns = [
    path('country-list/', views.CountryListView.as_view()),
    path('country-add/', views.CountryAddView.as_view()),
    path('country-details-<int:pk>/', views.CountryDetailView.as_view()),
]


# authorization
urlpatterns += [
    path('create-user/', views.CreateUserAPIView.as_view()),
    path('update-user/', views.UserRetrieveUpdateAPIView.as_view()),
]


# token
urlpatterns += [
    path('token/', TokenObtainPairView.as_view()),
    path('token-refresh', TokenRefreshView.as_view()),
]


# add path for google authentication
urlpatterns += [
    path('google/', views.GoogleView.as_view(), name='google'),
]


# viewsets
router = routers.DefaultRouter()
router.register('city', views.CityAddView)
urlpatterns += [
    path('', include(router.urls)),
]