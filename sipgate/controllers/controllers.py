# -*- coding: utf-8 -*-
from odoo import http

# class Sipgate(http.Controller):
#     @http.route('/sipgate/sipgate/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sipgate/sipgate/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('sipgate.listing', {
#             'root': '/sipgate/sipgate',
#             'objects': http.request.env['sipgate.sipgate'].search([]),
#         })

#     @http.route('/sipgate/sipgate/objects/<model("sipgate.sipgate"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sipgate.object', {
#             'object': obj
#         })