# -*- coding: utf-8 -*-
# from odoo import http


# class Sqlassistant(http.Controller):
#     @http.route('/sqlassistant/sqlassistant', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sqlassistant/sqlassistant/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('sqlassistant.listing', {
#             'root': '/sqlassistant/sqlassistant',
#             'objects': http.request.env['sqlassistant.sqlassistant'].search([]),
#         })

#     @http.route('/sqlassistant/sqlassistant/objects/<model("sqlassistant.sqlassistant"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sqlassistant.object', {
#             'object': obj
#         })
