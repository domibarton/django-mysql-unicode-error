# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.views.generic import View
from django.http import HttpResponse
from .models import MyFirstModel, MySecondModel


class PrepareView(View):

    def get(self, request, *args, **kwargs):

        first = MyFirstModel(
            value1='Hellö',
            value2='Hellö',
        )

        second = MySecondModel(
            value='Testing'
        )

        first.save()
        second.save()

        return HttpResponse('Prepare finished, now call the test view…')


class TestView(View):

    def get(self, request, attr, *args, **kwargs):

        first  = MyFirstModel.objects.get(id=1)
        second = MySecondModel.objects.get(id=1)

        #
        # When we're now accessing the `first.value1` property, the object will
        # return a `unicode` object which is fine! This is what we expect.
        #
        # However, if we're now accessing the `first.value2` property, the
        # object will return a `str` instead of a `unicode` object and thus
        # we'll get a `UnicodeError` when we're assigning the value to our
        # `second.value` property, as the object cannot decode the value!
        #
        # IMHO this is because the MySQL lib is not properly programmed as it
        # checks directly for a `unicode` object instead of checking the
        # inheritance of the value/object.
        #

        second.value = getattr(first, attr)
        second.save()

        return HttpResponse('All fine mate…')
