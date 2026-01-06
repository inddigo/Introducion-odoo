from odoo import models, fields

class ResUsers(models.Model): 
    _inherit = 'res.users'

    unidad_ids = fields.Many2many(
        'modulo_introduccion.unidad_negocio',
        string='Unidades de Negocio Asignadas'
    )