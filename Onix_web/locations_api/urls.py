# -*- coding: utf-8 -*-
from django.urls import path, include
from locations_api import views
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from locations_api.yasg import urlpatterns as doc_urls

app_name = 'locations_api'

urlpatterns = [
    # generics
    path('countries/', views.CountryListView.as_view(), name='countries'),
    path('countries-add/', views.CountryAddView.as_view(), name='countries_add'),
    path('countries-details/<int:pk>/', views.CountryDetailView.as_view(), name='countries_details'),
    # authorization
    path('users/', views.CreateUserAPIView.as_view(), name='users_create'),
    path('users-update/', views.UserRetrieveUpdateAPIView.as_view()),
    # token
    path('token/', TokenObtainPairView.as_view()),
    path('token-refresh/', TokenRefreshView.as_view()),
    # add path for google authentication
    path('google/', views.GoogleView.as_view(), name='google'),
]

# drf_yasg
urlpatterns += doc_urls


# viewsets
router = routers.DefaultRouter()
router.register('cities', views.CityAddView)
urlpatterns += [
    path('', include(router.urls)),
]
