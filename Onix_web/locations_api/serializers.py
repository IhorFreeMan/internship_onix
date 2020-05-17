# -*- coding: utf-8 -*-
from locations_api.models import MyNotebook
from rest_framework import serializers


class MyNotebookSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyNotebook
        fields = '__all__'
