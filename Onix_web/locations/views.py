# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from locations.models import Country, City, Symbol
from locations.forms import AddCountryForm, CityForm

@login_required
def country_directory(request):
    """list of countries"""
    category_list = Country.objects.order_by()
    return render(request, 'locations/categories_countries.html', {'categories': category_list})


@login_required
def country_detail(request, id_city):
    """country in detail"""
    try:
        country = Country.objects.get(pk=id_city)
    except City.DoesNotExist:
        pass
    return render(request, 'locations/country_detail.html', {'country': country})

@login_required
def city_detail(request, id):
    """city ​​in detail"""
    city = get_object_or_404(City, id=id)
    return render(request, 'locations/city_detail.html', {'city': city})


@login_required
def delete_city(request, id):
    """delete city"""
    city_del = get_object_or_404(City, id=id)
    country_id = city_del.country_id
    city_del.delete()
    return redirect('locations:country_detail', country_id)


@login_required
def add_country(request):
    """add country"""
    if request.method == 'POST':
        form = AddCountryForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            country = form.save(commit=False)
            country.save()
            return redirect('locations:country_directory')
    else:
        form = AddCountryForm
    return render(request, 'locations/add_country.html', {'form': form})


@login_required
def edit_country(request, id):
    country = get_object_or_404(Country, pk=id)
    form = AddCountryForm(request.POST, instance=country)
    if request.method == 'POST':
        if form.is_valid():
            country = form.save(commit=False)
            country.save()
            return redirect('locations:country_detail', id_city=id)
    else:
        form = AddCountryForm(instance=country)
    return render(request, 'locations/edit_country.html', {'form': form})


@login_required
def add_city(request):
    """add city"""
    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            city = form.save(commit=False)
            city.save()
            return redirect('locations:country_directory')
    else:
        form = CityForm
    return render(request, 'locations/add_city.html', {'form': form})


@login_required
def edit_city(request, id):
    city = get_object_or_404(City, pk=id)
    form = CityForm(request.POST, instance=city)
    if request.method == 'POST':
        if form.is_valid():
            city = form.save(commit=False)
            city.save()
            return redirect('locations:city_detail', city.pk)
    else:
        form = CityForm(instance=city)
    return render(request, 'locations/edit_city.html', {'form': form})