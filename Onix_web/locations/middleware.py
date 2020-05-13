# -*- coding: utf-8 -*-
from django.utils.deprecation import MiddlewareMixin
from locations.models import Country

class MyTestMiddleware(MiddlewareMixin):
    def process_request(self, request):
        # country = Country.objects.all()
        # request['country'] = country
        return print('My test Middleware')




