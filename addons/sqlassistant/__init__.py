from odoo import api, SUPERUSER_ID
from odoo.http import request

def post_init_hook(cr, registry):
    env = api.Environment(cr, SUPERUSER_ID, {})
    http_routing = env.ref('base.module_category_website')
    http_routing.children_ids.create(name='My Module', url='/my_module/hello')

    request.registry['ir.http']._add_route('my_module', '/my_module/hello', 'sqlassistant.controllers.MyModuleController', '_call', auth='public')