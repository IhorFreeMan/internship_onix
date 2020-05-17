from django.shortcuts import render
from locations_api.models import MyNotebook
from rest_framework import generics
from locations_api.serializers import MyNotebookSerializer


# List objects Api
class ArticleListView(generics.ListAPIView):
    serializer_class = MyNotebookSerializer
    queryset = MyNotebook.objects.order_by('-data')

