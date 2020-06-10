# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
from locations.models import Country
import re


class Command(BaseCommand):
    help = """will take a string, display in the console a 
    list of countries and status, is there a line in the name of the country"""

    def add_arguments(self, parser):
        # We indicate how many and what arguments the team takes.
        # In this case, this is one argument of type str.
        parser.add_argument('word_search', nargs=1, type=str)

    def handle(self, *args, **kwargs):
        category_list = Country.objects.order_by()
        word_search = kwargs['word_search'][0]
        word_search_lower = str(word_search).lower()

        for country in range(len(category_list)):
            country_lower = str(category_list[country]).lower()
            result = re.search(r'%s' % word_search_lower, country_lower)

            if result:
                print(category_list[country], 'True')
            else:
                print(category_list[country], 'False')

