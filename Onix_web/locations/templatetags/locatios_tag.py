# -*- coding: utf-8 -*-
from django import template
from locations.models import Country

register = template.Library()


@register.simple_tag(name='my_count_country_tag')
def count_country_tag():
    return Country.objects.order_by().count()


