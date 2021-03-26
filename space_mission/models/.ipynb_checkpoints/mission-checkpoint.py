# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import timedelta

class Mission(models.Model):
    _name = 'space.mission'
    _description = 'Space Missions'
    
    spaceship_id = fields.Many2one(comodel_name='space.spaceship',
                                  string='Spaceship',
                                  ondelete='cascade',
                                  required=True)
    
    name = fields.Char(string='Mission', required=True)
    
    ship = fields.Char(string='Vessel', related='spaceship_id.name', required=True)
    
    crew_members = fields.Many2many(comodel_name='res.partner',string='Crew Members')
    
    captain = fields.Many2one(comodel_name='res.partner', string='Captain')
    
    launch_date = fields.Date(string='Start Date',
                            default=fields.Date.today)
    
    duration = fields.Integer(string='Duration',
                             default=1)
    
    return_date = fields.Date(string='Return Date',
                             compute='_compute_return_date',
                             inverse='_inverse_end_date',
                             store=True)
    
    @api.depends('launch_date','duration')
    
    def _compute_return_date(self):
        for record in self:
            if not (record.launch_date and record.duration):
                record.return_date = record.launch_date
            else:
                duration_days = timedelta(days=record.duration)
                record.return_date = record.launch_date + duration_days
                
    def _inverse_end_date(self):
        for record in self:
            if record.launch_date and record.return_date:
                record.duration = (record.return_date - record.launch_date).days
            else:
                continue