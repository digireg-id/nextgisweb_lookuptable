# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os.path

from pyramid.response import FileResponse
from pyramid.httpexceptions import HTTPNotFound

from nextgisweb.resource import Resource, Widget, resource_factory, DataScope
from nextgisweb.env import env
from .model import LookupTable


class Widget(Widget):
    resource = LookupTable
    operation = ('create', 'update')
    amdmod = 'ngw-lookup-table/Widget'


def setup_pyramid(comp, config):
    pass
