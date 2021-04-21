# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError
from odoo.addons.website.tools import get_video_embed_code

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
    
    mission_count = fields.Integer(string='Mission Count',
                                  compute='get_mission_count',
                                  store=True,
                                  default=False)
    
    video_url = fields.Char('Video URL',
                           help='URL of a video')
    
    embed_code = fields.Char(compute="_compute_embed_code")
    
    @api.depends('video_url')
    def _compute_embed_code(self):
        for image in self:
            image.embed_code = get_video_embed_code(image.video_url)
    
    @api.depends('mission_ids')
    def get_mission_count(self):
        for record in self:
            count = record.env['space.mission'].search_count([('spaceship_id','=',record.id)])
            record.mission_count = count
  
    
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
   
    def open_missions(self):
        return {
            'name': 'Missions',
            'domain': [('spaceship_id','=',self.id)],
            'view_type': 'form',
            'res_model':'space.mission',
            'view_id':False,
            'view_mode':'tree,form',
            'type':'ir.actions.act_window',            
        }