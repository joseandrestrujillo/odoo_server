from odoo import models, fields, api

class SqlAssistant(models.Model):
    _name = 'model_sql_assistant'
    _description = 'SQL Assistant'

    query = fields.Char()
    result = fields.Text(readonly=True)

    @api.multi
    def execute_query(self):
        self.ensure_one()
        self.result = 'TODO: Implement query execution'
