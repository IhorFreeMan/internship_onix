# -*- coding: utf-8 -*-
# main/tasks.py

import logging

from celery import shared_task
from django.urls import reverse
from django.core.mail import send_mail
from django.contrib.auth import get_user_model
from Onix_web.celery import app


@app.task
def country_created(mail):
    subject = 'Country created'
    message = 'Congratulations! Your country was successfully added!'
    send_mail(subject,
              message,
              'admin@admin.com',
              [mail])


@app.task
def country_update(mail, name, link_for_view_country):
    subject = 'Country update'
    message = f'Your country {name} was changed. You can view changes at {link_for_view_country}'
    send_mail(subject,
              message,
              'admin@admin.com',
              [mail])


@app.task
def periodic_task():
    print('periodic-task-20-min')
