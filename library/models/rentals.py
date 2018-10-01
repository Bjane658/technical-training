# -*- coding: utf-8 -*-
from odoo import models, fields, api, exceptions, _

class Rentals(models.Model):
    _name = 'library.rental'
    _description = 'Book rental'

    customer_id = fields.Many2one('library.partner', string='Customer')
    book_id = fields.Many2one('library.book', string='Book')
    rental_date = fields.Date(string='Rental date')
    return_date = fields.Date(string='Return date')
    customer_mail = fields.Char(string='CustomerMail', related='customer_id.email', store=True)
 #   customer_address = fields.Char(string="CustomerAddress", related='customer_id.address')

    # book_author_ids = fields.Many2many(related='book_id.authors_ids', store=True)
    
    all_the_names = fields.Char(string='All the authors', compute='_compute_all_names')
    
    def _compute_all_names(self):
        self.all_the_names = ', '.join(self.book_id.mapped('authors_ids.name'))
    
