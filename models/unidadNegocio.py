from odoo import models, fields

class UnidadNegocio(models.Model):
    _name = 'modulo_introduccion.unidad_negocio'
    _description = 'Unidad de Negocio'





    name = fields.Char(string='Nombre', required=True)

    