# -*- coding: utf-8 -*-
from django.db import models

class MyNotebook(models.Model):
    name = models.CharField(max_length=50)
    text = models.TextField()
    data = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.name


