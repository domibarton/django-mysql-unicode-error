# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.db.models import TextField


class KeyValue(unicode):
    pass


class KeyValueField(TextField):

    def from_db_value(self, value, expression, connection, context):
        return KeyValue(value)
