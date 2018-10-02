# -*- coding: utf-8 -*-
from odoo import models, fields

class Books(models.Model):
    _name = 'library.book'
    _description = 'Book'

    name = fields.Char(string='Title')
    authors_ids = fields.Many2many('library.partner', string="Authors")
    edition_date =  fields.Date(string='Edition date',)
    isbn = fields.Char(string='ISBN')
    publisher_id = fields.Many2one('library.publisher', string='Publisher')
    #copy_ids = fields.One2many('library.book_copy', 'book_id', string='Rentals')


    
class Book_copy(models.Model):
    _name = 'library.book_copy'
    _inherits = {'library.book': 'book_id'}
    
#    book_id = fields.Many2one('library.book', string='Book')
    customer_id = fields.Many2one('library.partner', string='Customer')
    
    
    
    
    