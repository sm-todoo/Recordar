# -*- coding: utf-8 -*-
# from odoo import http


# class Fundacion(http.Controller):
#     @http.route('/fundacion/fundacion/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/fundacion/fundacion/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('fundacion.listing', {
#             'root': '/fundacion/fundacion',
#             'objects': http.request.env['fundacion.fundacion'].search([]),
#         })

#     @http.route('/fundacion/fundacion/objects/<model("fundacion.fundacion"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('fundacion.object', {
#             'object': obj
#         })
