from odoo import models, api

class  ReporteProducto(models.AbstractModel):
    _name = 'report.modulo_introduccion.report_producto_template'
    _description = 'Logica Diccionario Reporte de Productos'

    @api.model
    def _get_report_values(self, docids, data=None):

        ##busca la info en odoo y trae los dattos de los ids 
        docs = self.env['modulo_introduccion.producto'].browse(docids)

        ##guarda la info de cada producto seleccionado
        lista_productos =[]
        for i in docs:
            info ={
                
                'codigo': i.codigo,
                'descripcion': i.descripcion,
                'tipo': i.tipo,
                'origen': i.origen,
                'unidad_negocio':i.unidad_ids.mapped('name'),
                'elementos':[{'nombre': parte.name} for parte in i.parte_ids], ##lista con partes
            }
            ##lista guarda el diccionario
            lista_productos.append(info)    

        print("DATOS ENVIADOS AL PDF:", lista_productos)
        return{
            'doc_ids': docids,
            'doc_model': 'modulo_introduccion.producto',
            'data_pdf':lista_productos,
}