# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from pkg_resources import resource_filename
from nextgisweb.component import Component, require

from .model import Base


@Component.registry.register
class LookupTableComponent(Component):
    identity = 'lookup_table'
    metadata = Base.metadata

    def initialize(self):
        pass

    def setup_pyramid(self, config):
        from . import view  # NOQA
        view.setup_pyramid(self, config)


def pkginfo():
    return dict(components=dict(
        lookup_table="nextgisweb_lookuptable"))


def amd_packages():
    return ((
        'ngw-lookup-table', 'nextgisweb_lookuptable:amd/ngw-lookup-table'),
    )
