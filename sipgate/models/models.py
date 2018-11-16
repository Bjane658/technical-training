# -*- coding: utf-8 -*-

from odoo import models, fields, api
import os

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
    
    
    
    #Hier ist in der Authorization der Key rausgenommen, der muss wieder reingefuegt werden, bze aus den Stammdaten bezogen werden
    def call_partner(self):
        # self.env.user.phone funktioniert auch nicht, der button click geht ins leere
        #currentUser = self.pool.get('res.users').browse(cr, uid, uid, context=context).phone
        currentUser = "+4921152800935"
        os.system("curl -X POST 'https://api.sipgate.com/v2/sessions/calls' -H 'Authorization: Basic ###########'-H 'accept: application/json' -H 'Content-Type: application/json' -d '{ \"deviceId\": \"e6\", \"caller\": \"" + currentUser + " \", \"callee\": \"" + self.phone + " \", \"callerId\": \"+4921152800935\"}'")
