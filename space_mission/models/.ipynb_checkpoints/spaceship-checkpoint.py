# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError

class Spaceship(models.Model):
    
    _name = 'space.spaceship'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Spaceship Info'
    
    name = fields.Char(string='Name', required=True)
    ship_type = fields.Selection(string='Type',
                                selection=[('fighter','Fighter'),
                                          ('exploration','Exploration'),
                                          ('cruise','Cruise')],
                                copy=False)
    length = fields.Float(string='Length', default=0.00)
    width = fields.Float(string='Width', default=0.00)
    description = fields.Text(string='Description')
    engines = fields.Integer(string='Number of Engines', default=1)
    fuel_type = fields.Text(string='Fuel Type')
    number_of_passengers = fields.Integer(string='Number of Passengers')
    ship_image = fields.Image(string="Ship Image")
    
    active = fields.Boolean(string='Active', default=True)
    
    mission_ids = fields.One2many(comodel_name='space.mission',
                                 inverse_name='spaceship_id',
                                 string='Missions')
    
    
    @api.constrains('length','width')
    
    def _check_ship_size(self):
        for record in self:
            if record.width > record.length:
                raise UserError('Width can not be bigger than the length')
    
    def print_spaceship(self):
        self.ensure_one()
        return {
            'type':'ir.actions.report',
            'model':'space.spaceship',
            'report_name':'space_mission.spaceship_report_template',
            'report_type':'qweb-html',
            'name':'Spaceship Report',
        }