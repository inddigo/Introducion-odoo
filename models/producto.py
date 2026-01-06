from odoo import models, fields


class Producto(models.Model):
    _name = 'modulo_introduccion.producto'
    _description = 'Modelo de productos'

    name = fields.Char(string='Nombre', required=True) 
    tipo = fields.Selection([('bien', 'Bien'),
                             ('servicio', 'Servicio')
                            ], string='Tipo', default='bien')
    codigo = fields.Char(string='Código', copy=False)
    descripcion = fields.Text(string ='Descripción')
    origen = fields.Selection([
        ('imp', 'IMP'),
        ('nac', 'NAC') 
    ], string = 'Origen')
    cantidad_vendida = fields.Float(string='Cantidad Vendida')


    unidad_ids = fields.Many2many(
    'modulo_introduccion.unidad_negocio', # Modelo destino
    'producto_unidad_rel',                # NOMBRE DE LA TABLA (Corto para evitar el error)
    'producto_id',                        # Columna para este modelo
    'unidad_id',                          # Columna para el modelo destino
    string='Unidades de Negocio'
)


    parte_ids = fields.One2many('modulo_introduccion.parte', 'producto_id', string='Partes')

#Restriccion a codigo unico
    _sql_constraints = [
        ('codigo_unique', 'unique(codigo)', 'El código del producto debe ser único.')
    ]


    

