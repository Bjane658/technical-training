
from odoo import models, api, fields


class Book(models.Model):
    
    _name = 'library.book'
    
    title = fields.Char(string='Title')
    release = fields.Date(string='ReleaseDate')
    isbn = fields.Char(string='ISBN')
    
    
    Author = fields.One2many('library.Author', string='Author')
    Editor = fields.One2many('library.Editor', string='Editor')
    Customer = fields.One2many('library.Customer', string='Customer')
    

class Author(models.Model):
    _name = 'library.author'
    
    name = fields.Char(string='Name')


class Editor(models.Model):
    _name = 'library.editor'
    
    name = fields.Char(string='Name')
    
class Customer(models.Model):
    _name = 'library.customer'
    
    name = fields.Char(string='Name')
    adress = fields.Text(string='Adress')
