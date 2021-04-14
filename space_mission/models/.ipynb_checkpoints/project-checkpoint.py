# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Project(models.Model):
    _inherit = 'project.project'
    
    mission_id = fields.Many2one(comodel_name='space.mission',
                                string='Related Mission',
                                ondelete='set null')
    
    captain = fields.Many2one(string='Captain',
                             related='mission_id.captain')
    
    crew_members = fields.Many2many(string='Crew Members',
                                   related='mission_id.crew_members')