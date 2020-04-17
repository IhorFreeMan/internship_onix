# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render

def test_views(request):
    return HttpResponse('Зарабтало, Ура!')

def test_views_one(request, add_something):
    return render(request, 'test.html', {'press': add_something})
