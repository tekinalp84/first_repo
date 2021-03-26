# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Spaceship(models.Model):
    
    _name = 'space.spaceship'
    _description = 'Spaceship Info'
    
    name = fields.Char(string='Name', required=True)
    ship_type = fields.Selection(string='Type',
                                selection=[('fighter','Fighter'),
                                          ('exploration','Exploration'),
                                          ('cruise','Cruise')],
                                copy=False)
    dimensions = fields.Text(string='Dimensions')
    description = fields.Text(string='Description')
    fuel_type = fields.Text(string='Fuel Type')
    number_of_passengers = fields.Integer(string='Number of Passengers')
    ship_image = fields.Binary(string="Ship Image")
    
    active = fields.Boolean(string='Active', default=True)
    