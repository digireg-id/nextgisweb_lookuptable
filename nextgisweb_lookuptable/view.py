# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from nextgisweb.resource import Widget
from .model import LookupTable


class Widget(Widget):
    resource = LookupTable
    operation = ('create', 'update')
    amdmod = 'ngw-lookup-table/Widget'


def setup_pyramid(comp, config):
    pass
