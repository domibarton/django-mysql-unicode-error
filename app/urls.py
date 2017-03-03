# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.conf.urls import url
from .views import *

urlpatterns = (
    url(r'^prepare/$', PrepareView.as_view()),
    url(r'^test/(?P<attr>value[12])/$', TestView.as_view()),
)
