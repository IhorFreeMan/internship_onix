# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from locations.models import (Country,
                              City)

@login_required
def country_directory(request):
    """list of countries"""
    category_list = Country.objects.order_by()
    context_dict = {'categories': category_list}
    return render(request, 'locations/categories_countries.html', context_dict)

@login_required
def country_detail(request, id_city):
    """country in detail"""
    try:
        category_list_city = City.objects.filter(country_id=id_city)
        country_list = Country.objects.filter(pk=id_city).first()
    except City.DoesNotExist:
        pass
    return render(request, 'locations/country_detail.html', {'category_list_city':category_list_city,
                                                             'country_list':country_list,})

@login_required
def city_detail(request, id):
    """city ​​in detail"""
    try:
        city_detail_list = City.objects.filter(id=id)
    except City.DoesNotExist:
        pass
    return render(request, 'locations/city_detail.html', {'city_detail':city_detail_list})


@login_required
def delete_city(request, id):
    """delete city"""
    city_del = get_object_or_404(City, id=id)
    country_id = city_del.country_id
    city_del.delete()
    return redirect(f'/locations/country_detail={country_id}')