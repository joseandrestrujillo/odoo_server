# -*- coding: utf-8 -*-

from . import controllers
from . import models
from odoo import api, SUPERUSER_ID
from odoo.http import request

def post_init_hook(cr, registry):
    env = api.Environment(cr, SUPERUSER_ID, {})
    http_routing = env.ref('base.module_category_website')
    http_routing.children_ids.create(name='SQL Assistant', url='/sqlassistant/sqlassistant')

    request.registry['ir.http']._add_route('sqlassistant', '/sqlassistant/sqlassistant', 'sqlassistant.controllers.Sqlassistant', '_call', auth='public')