from odoo import models, fields

class MyModuleModel(models.Model):
    _name = 'my.module.model'
    name = fields.Char()
    description = fields.Char()