# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from nextgisweb.resource import Widget, Resource
from .model import LookupTable


class Widget(Widget):
    resource = LookupTable
    operation = ('create', 'update')
    amdmod = 'ngw-lookup-table/Widget'


def setup_pyramid(comp, config):
    #Регистрируем секцую
    Resource.__psection__.register(
       key='focl_project', priority=10,
       is_applicable=lambda obj: isinstance(obj, LookupTable),
       template='nextgisweb_lookuptable:/template/lookuptable_section.mako')
