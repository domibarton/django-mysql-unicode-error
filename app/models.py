# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.db import models
from .keyvalue import KeyValueField


class MyFirstModel(models.Model):

    # This field is working as expected!
    value1 = models.TextField(default='', blank=True)

    # This field will fail, as it returns its value not as `unicode` object!
    value2 = KeyValueField(default='', blank=True)


class MySecondModel(models.Model):
    value = models.TextField(default='', blank=True)
