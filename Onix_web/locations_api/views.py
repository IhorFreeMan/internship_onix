# -*- coding: utf-8 -*-
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.status import HTTP_201_CREATED, HTTP_200_OK, HTTP_403_FORBIDDEN
from locations.models import Country, City
from rest_framework import viewsets, generics
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny
from locations_api.serializers import (CountriesSerializer,
                                       CountryAddSerializer, CountryDetailSerializer, CitySerializer, UserAddSerializer)
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.hashers import make_password
from rest_framework.utils import json
from rest_framework.views import APIView
from rest_framework.response import Response
import requests
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from locations_api.tasks import country_created, country_update


class CountryListView(generics.ListAPIView):
    """List Country"""
    queryset = Country.objects.all()
    serializer_class = CountriesSerializer
    permission_classes = [IsAuthenticated]


class CountryAddView(generics.CreateAPIView):
    """Create Country"""
    serializer_class = CountryAddSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            country = serializer.save()
            task = country_created.delay(request.user.email)
            return Response({'task': request.user.email})
        else:
            return Response({"error": serializer.errors})



class CountryDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Update Destroy Country"""
    queryset = Country.objects.all()
    serializer_class = CountryDetailSerializer
    permission_classes = [IsAuthenticated]

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)

        if serializer.is_valid():
            country = serializer.save()
            my_url = str(request.get_host()) + str(request.path)
            task = country_update.delay(request.user.email, country.name, my_url)

        self.perform_update(serializer)
        return Response(serializer.data)



class CityAddView(viewsets.ModelViewSet):
    """Add City end Country. List City end Country"""
    serializer_class = CitySerializer
    queryset = City.objects.all()
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['country_id']


class CreateUserAPIView(generics.CreateAPIView):
    """Create User"""
    serializer_class = UserAddSerializer


class UserRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    """ User Retrieve Update"""
    # Allow only authenticated users to access this url
    permission_classes = (IsAuthenticated,)
    serializer_class = UserAddSerializer

    def get(self, request, *args, **kwargs):
        # serializer to handle turning our `User` object into something that
        # can be JSONified and sent to the client.
        serializer = self.serializer_class(request.user)

        return Response(serializer.data, status=HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        serializer_data = request.data.get('user', {})

        serializer = UserAddSerializer(
            request.user, data=serializer_data, partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=HTTP_200_OK)


class GoogleView(APIView):
    def post(self, request):
        payload = {'access_token': request.data.get("token")}
        r = requests.get('https://www.googleapis.com/oauth2/v2/userinfo', params=payload)
        data = json.loads(r.text)

        if 'error' in data:
            content = {'message': 'wrong google token / this google token is already expired.'}
            return Response(content)

        try:
            user = User.objects.get(email=data['email'])
        except User.DoesNotExist:
            user = User()
            user.username = data['email']
            user.password = make_password(BaseUserManager().make_random_password())
            user.email = data['email']
            user.save()

        token = RefreshToken.for_user(user)
        response = {}
        response['username'] = user.username
        response['access_token'] = str(token.access_token)
        response['refresh_token'] = str(token)
        return Response(response)
