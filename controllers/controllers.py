# -*- coding: utf-8 -*-
# from odoo import http


# class ModuloIntroduccion(http.Controller):
#     @http.route('/modulo_introduccion/modulo_introduccion', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/modulo_introduccion/modulo_introduccion/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('modulo_introduccion.listing', {
#             'root': '/modulo_introduccion/modulo_introduccion',
#             'objects': http.request.env['modulo_introduccion.modulo_introduccion'].search([]),
#         })

#     @http.route('/modulo_introduccion/modulo_introduccion/objects/<model("modulo_introduccion.modulo_introduccion"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('modulo_introduccion.object', {
#             'object': obj
#         })

