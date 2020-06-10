# -*- coding: utf-8 -*-

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from locations.models import Country, City, Symbol
from django.contrib.auth.models import User
from locations_api.serializers import CountryDetailSerializer

class LocationsApiTests(APITestCase):

    def setUp(self):
        self.symbol = Symbol.objects.create(image='country/2020/05/25/art3.jpg')
        self.user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
        self.country = Country.objects.create(flag=self.symbol, name="Занзібар", description="description-Занзібар", population=100)
        self.country.users.add(self.user)
        self.country.save()

        City.objects.create(name='Київ', country=self.country, longitude=1, latitude=1)
        self.symbol2 = Symbol.objects.create(image='country/2020/05/24/P90727-092924.jpg')

        self.data = {
            "name": "Єгиипет",
            "description": "description",
            "population": 200,
            "flag": self.symbol2.id,
            "users": self.user.id,
            "cities_count": 1
        }

        self.data_city = {
            "name": "Львів",
            "country": self.country.pk,
            "longitude": 2.0,
            "latitude": 2.0
        }

        self.add_user = {
            'id': 3,
            'username': 'username3',
            'first_name': 'first_name',
            'last_name': 'last_name',
            'email': 'fff@gmail.com',
            'password': 123,
        }

        self.user = User.objects.get(username='john')
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_country_list(self):
        """"""
        response = self.client.get(reverse('locations_api:countries'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data[0]), 6)
        self.assertEqual(response.json()[0].get('name'), 'Занзібар')
        self.assertEqual(response.json()[0].get('description'), 'description-Занзібар')
        self.assertEqual(response.json()[0].get('population'), 100)


    def test_country_detail(self):
        """"""
        response = self.client.get(reverse('locations_api:countries_details', kwargs={'pk': self.country.pk}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)



    def test_city_list(self):
        response = self.client.get('/api/cities/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data[0]), 4)
        self.assertEqual(response.json()[0].get('name'), 'Київ')
        self.assertEqual(response.json()[0].get('country'), 1)
        self.assertEqual(response.json()[0].get('longitude'), 1)
        self.assertEqual(response.json()[0].get('latitude'), 1)


    def test_city_post(self):
        response = self.client.post('/api/cities/', self.data_city, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


    def test_user_create(self):
        response = self.client.post(reverse('locations_api:users_create'), self.add_user, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)



















