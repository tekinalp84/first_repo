# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Spaceship(models.Model):
    _name = 'space.spaceship'
    _description = 'Spaceship Info'
    
    name = fields.Char(string='Title', required=True)
    description = fields.Text(string='Description')