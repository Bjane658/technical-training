# -*- coding: utf-8 -*-

from odoo import models, fields, api

class sipgate(models.Model):
    _name = 'sipgate.sipgate'

    name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100

class sipCall(models.Model):
   # _name = 'sipgate.callsip'
    _inherit = 'res.partner'
    
    favColor = fields.Char(string="FavColor")