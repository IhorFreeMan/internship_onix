# -*- coding: utf-8 -*-
from django.urls import path
from locations import views


urlpatterns = [
    path('test_views/', views.test_views),
    path('test_views_one/<str:add_something>', views.test_views_one),
]




