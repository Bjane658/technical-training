from odoo import models, api, fields


class Course(models.Model):
    _name = 'openacademy.course'
    
    name = fields.Char(string='Name')
    description = fields.Text(string='Description')
    responsible_id = fields.Many2one('res.partner', string='Responsible')
    level_id = fields.Many2one('openacademy.level', string='Level')
    maester_id = fields.Many2one('openacademy.maester', string='Maester')
    datetime_id = fields.One2many('openacademy.session', 'course_id', string='Sessions', onedelete='cascade')
    
class Level(models.Model):
    _name = 'openacademy.level'
    
    name = fields.Char(string='Name')
    description = fields.Text(string='Description')
    
    
class Maester(models.Model):
    _name = 'openacademy.maester'
    
    name = fields.Char(string='Name')
    despriptions = fields.Text(string='Description')
    
class Session(models.Model):
    
    _name = 'openacademy.session'
    
    
    name = fields.Char(name='Name')
    datetime = fields.Datetime(string='Datetime')
    course_id = fields.Many2one('openacademy.course', string='Course')