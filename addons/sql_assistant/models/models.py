# -*- coding: utf-8 -*-

from .sql_traslator import SQL_Traslator
from odoo import models, fields, tools, api
import psycopg2
import psycopg2.extras
import json
from datetime import datetime

api_key=""
traslator = SQL_Traslator(api_key=api_key)

class sql_assistant_record(models.Model):
    _name = 'sql_assistant.record'
    _description = 'SQL Assistant Record'

    sql_assistant_id = fields.Many2one('sql_assistant.sql_assistant', ondelete='cascade')
    message_main_attachment_id = fields.Char(string='message_main_attachment_id')
    name = fields.Char(string='name')
    currency_id = fields.Char(string='currency_id')
    code = fields.Char(string='code')
    deprecated = fields.Char(string='deprecated')
    user_type_id = fields.Char(string='user_type_id')
    internal_type = fields.Char(string='internal_type')
    internal_group = fields.Char(string='internal_group')
    reconcile = fields.Char(string='reconcile')
    note = fields.Char(string='note')
    company_id = fields.Char(string='company_id')
    group_id = fields.Char(string='group_id')
    root_id = fields.Char(string='root_id')
    is_off_balance = fields.Char(string='is_off_balance')
    create_uid = fields.Char(string='create_uid')
    create_date = fields.Char(string='create_date')
    write_uid = fields.Char(string='write_uid')
    write_date = fields.Char(string='write_date')

class sql_assistant(models.Model):
    _name = 'sql_assistant.sql_assistant'
    _description = 'sql_assistant.sql_assistant'


    prompt = fields.Text(string='Consulta')
    record_ids = fields.One2many('sql_assistant.record', 'sql_assistant_id', string='Records')

    def datetime_to_string(self, data):
        for item in data:
            for key, value in item.items():
                if isinstance(value, datetime):
                    item[key] = value.strftime('%Y-%m-%d %H:%M:%S')
        return data

    def fields_view_get(self, cr, uid, view_id=None, view_type='form', context=None, toolbar=False,submenu=False):
        result = super(self._name, self).fields_view_get(cr, uid, view_id, view_type, context, toolbar,submenu)

    def execute_query(self):
        #sql_query = traslator.convert_to_sql(text_for_query=self.prompt)
        sql_query = self.prompt
        self.env.cr.execute(sql_query)
        records = self.env.cr.dictfetchall()
        self.record_ids.unlink()
        records = self.datetime_to_string(records)
        # Crear vista de árbol dinámicamente
        tree_view = self.env['ir.ui.view'].create({
            'name': 'sql_assistant.record.tree',
            'type': 'tree',
            'model': 'sql_assistant.record',
            'arch': self._generate_tree_view_arch(records),
        })

        # Actualizar la relación entre la vista y el campo 'record_ids'
        self.write({
            'record_ids': [(6, 0, [r.id for r in tree_view])]
        })

        # Crear registros
        for record in records:
            self.env['sql_assistant.record'].create({
                'sql_assistant_id': self.id,
                **record
            })

    def _generate_tree_view_arch(self, records):
        if not records:
            return '<tree><field name="display_name"/></tree>'

        columns = records[0].keys()
        tree_view_arch = '<tree>'
        for col in columns:
            tree_view_arch += f'<field name="{col}"/>'
        tree_view_arch += '</tree>'
        return tree_view_arch