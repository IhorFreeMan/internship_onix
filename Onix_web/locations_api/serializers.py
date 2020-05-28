# -*- coding: utf-8 -*-
from rest_framework import serializers
from locations.models import Country, Symbol, City
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']


class SymbolSerializer(serializers.ModelSerializer):
    image = serializers.ImageField()
    class Meta:
        model = Symbol
        fields = ['image']


class CountriesSerializer(serializers.ModelSerializer):
    users = UserSerializer(many=True)
    flag = SymbolSerializer()

    class Meta:
        model = Country
        fields = ['name', 'flag', 'description', 'population', 'users', 'city_set']
        depth = 1


class CountryAddSerializer(serializers.ModelSerializer):
    # users = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault(), many=True)
    # flag = SymbolSerializer()
    class Meta:
        model = Country
        fields = ['name', 'flag', 'description', 'population', 'users']


class CountryDetailSerializer(serializers.ModelSerializer):
    users = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault(), many=True)
    class Meta:
        model = Country
        exclude = ['cities_count']


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['name', 'country', 'longitude', 'latitude']
