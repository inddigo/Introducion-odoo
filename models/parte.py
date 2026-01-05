from odoo import models, fields

class Parte(models.Model):
    _name = 'modulo_introduccion.parte'
    _description = 'Modelo de partes de un producto'

    name = fields.Char(string='Nombre', required=True)
    producto_id = fields.Many2one('modulo_introduccion.producto', string='Producto Referencia')
