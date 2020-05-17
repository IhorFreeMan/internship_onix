# -*- coding: utf-8 -*-
from django.urls import path
from locations_api import views

app_name = 'locations_api'

urlpatterns = [
    path('article_lists/', views.ArticleListView.as_view()),
]
