# -*- coding: utf-8 -*-

from odoo import models, fields, api
import psycopg2
import psycopg2.extras
import json

def get_tables(connection):
    cursor = connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

    cursor.execute("""SELECT table_schema, table_name
                      FROM information_schema.tables
                      WHERE table_schema != 'pg_catalog'
                      AND table_schema != 'information_schema'
                      AND table_type='BASE TABLE'
                      ORDER BY table_schema, table_name""")

    tables = cursor.fetchall()
    cursor.close()
    return tables


def format_tables_into_string(tables):
    val = ""
    for row in tables:
        val += "{}.{}\n".format(row["table_schema"], row["table_name"])
    return val


data_types = {
    "integer": "integer",
    "character varying": "varchar",
    "timestamp without time zone": "timestamp",
    "bytea": "bytea",
    "numeric": "numeric",
    "double precision": "double precision",
    "date": "date",
    "text": "text",
    "boolean": "boolean"
}

class sql_assistant(models.Model):
    conn = psycopg2.connect(database="odoodb",
                                user="odoo",
                                password="odoo15@2021",
                                host="db",
                                port="5432")
    

    _name = 'sql_assistant.sql_assistant'
    _description = 'sql_assistant.sql_assistant'


    query = fields.Text(string='Consulta')
    result = fields.Text(string='Resultado', readonly=True)

    

    def execute_query(self):
        query = self.query
        # self.result = format_tables_into_string(get_tables(self.conn))
        cur = self.conn.cursor()

        # Obtener el script de creación de la base de datos
        cur.execute("""SELECT table_name
                      FROM information_schema.tables
                      WHERE table_schema != 'pg_catalog'
                      AND table_schema != 'information_schema'
                      AND table_type='BASE TABLE'
                      ORDER BY table_name""")
        script = ""
        tables = cur.fetchall()
        for table in tables:
            table_name = table[0]
            cur.execute(f"SELECT column_name, data_type FROM information_schema.columns WHERE table_name = '{table_name}';")
            columns = cur.fetchall()
            create_table = f"CREATE TABLE {table_name} (" 
            for column in columns:
                tipo =data_types.get(column[1], "NO ESTA")
                create_table += f"{column[0]} {tipo},"
            create_table = create_table[:-1] + ");"
            
            script += create_table + "\n\n\n"
       
       # Cerrar el cursor y la conexión
        cur.close()
        
        self.result = script