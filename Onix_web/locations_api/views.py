# -*- coding: utf-8 -*-
from django_filters.rest_framework import DjangoFilterBackend
from locations.models import Country, City
from rest_framework import viewsets, generics
from rest_framework.permissions import IsAdminUser
from locations_api.serializers import (CountriesSerializer,
                                       CountryAddSerializer,
                                       CountryDetailSerializer,
                                       CitySerializer)


class CountryListView(generics.ListAPIView):
    """List Country"""
    queryset = Country.objects.all()
    serializer_class = CountriesSerializer
    permission_classes = [IsAdminUser]


class CountryAddView(generics.CreateAPIView):
    """Create Country"""
    serializer_class = CountryAddSerializer
    permission_classes = [IsAdminUser]


class CountryDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Update Destroy Country"""
    queryset = Country.objects.all()
    serializer_class = CountryDetailSerializer
    permission_classes = [IsAdminUser]


class CityAddView(viewsets.ModelViewSet):
    """Add City end Country. List City end Country"""
    serializer_class = CitySerializer
    queryset = City.objects.all()
    permission_classes = [IsAdminUser]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['country_id']
