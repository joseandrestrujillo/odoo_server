# -*- coding: utf-8 -*-
# from odoo import http


# class Sql-assistant(http.Controller):
#     @http.route('/sql-assistant/sql-assistant', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sql-assistant/sql-assistant/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('sql-assistant.listing', {
#             'root': '/sql-assistant/sql-assistant',
#             'objects': http.request.env['sql-assistant.sql-assistant'].search([]),
#         })

#     @http.route('/sql-assistant/sql-assistant/objects/<model("sql-assistant.sql-assistant"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sql-assistant.object', {
#             'object': obj
#         })
