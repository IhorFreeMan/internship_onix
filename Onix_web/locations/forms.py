# -*- coding: utf-8 -*-
from django.forms import ModelForm
from locations.models import Country, Symbol, City
from django import forms


class AddCountryForm(ModelForm):
    flag = forms.ImageField()
    class Meta:
        model = Country
        exclude = ['cities_count', 'users']

    def clean_flag(self):
        cleaned_data = self.cleaned_data
        cleaned_data = Symbol.objects.create(image=cleaned_data['flag'])
        return cleaned_data

class CityForm(ModelForm):
    class Meta:
        model = City
        fields = '__all__'


