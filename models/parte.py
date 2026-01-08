from odoo import models, fields

class Parte(models.Model):
    _name = 'modulo_introduccion.parte'
    _description = 'Modelo de partes de un producto'

    name = fields.Char(string='Nombre', required=True)
    producto_id = fields.Many2one('modulo_introduccion.producto', string='Producto Referencia')
    
    ##estado = fields.Selection([
        ##('sin_revisar', 'Sin Revisar'),
        ##('revisando', 'Revisando'),
      ##  ('revisado', 'Revisado')
    ##], string ='Estado', default='sin_revisar')



    # CORREGIDO: Ahora con paréntesis y nombre
    image = fields.Image("Imagen de la Parte")