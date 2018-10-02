# -*- coding: utf-8 -*-
from odoo import models, fields

class Partner(models.Model):
    _name = 'library.partner'

    name = fields.Char(string='Name')
    email = fields.Char(string='Email')
    address = fields.Text(string='Address')
    partner_type = fields.Selection([('customer', 'Customer'), ('author', 'Author')], default="customer")
    book_copy_ids = fields.One2many('library.book_copy', 'customer_id', string='Book_Copies')
