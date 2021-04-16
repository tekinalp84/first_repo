# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import timedelta


class Mission(models.Model):
    _name = 'space.mission'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Space Missions'
    _mail_post_access = 'read'
    
    spaceship_id = fields.Many2one(comodel_name='space.spaceship',
                                  string='Spaceship',
                                  ondelete='cascade',
                                  required=True)
    
    name = fields.Char(string='Mission', required=True, tracking=True)
    
    crew_members = fields.Many2many(comodel_name='res.partner',string='Crew Members')
    
    captain = fields.Many2one(comodel_name='res.partner', string='Captain',tracking=True)
    
    fuel_required = fields.Float(string='Amount of Fuel Needed', default=0.00)
    
    launch_date = fields.Date(string='Start Date',
                            default=fields.Date.today)
    
    duration = fields.Integer(string='Duration',
                             default=1)
    
    return_date = fields.Date(string='Return Date',
                             compute='_compute_return_date',
                             inverse='_inverse_end_date',
                             store=True)
    
    total_fuel = fields.Float(string='Total Consumed Fuel',
                              compute='_compute_total_fuel',
                              store=True)
    
    
    def _current_mission(self):
        return self.env['space.mission'].browse(self._context.get('active_id'))
    
    
    project_ids = fields.One2many(string='Projects',
                                 comodel_name='project.project',
                                 inverse_name='mission_id',
                                 default=_current_mission)
    
    state = fields.Selection(selection=[
        ('draft','Draft'),
        ('progress','In Progress'),
        ('complete','Completed'),
        ('cancel','Cancelled'),
    ],string='Status', required=True,readonly=True, copy=False, tracking=True,
    default='draft')
    
    @api.depends('fuel_required')
    def _compute_total_fuel(self):
        for r in self:
            r.total_fuel = r.fuel_required * r.spaceship_id.engines
    
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
                
    def button_draft(self):
        mission = self.env['space.mission']
        self.write({'state': 'draft'})
        
    def button_progress(self):
        mission = self.env['space.mission']
        self.write({'state': 'progress'})
        
    def button_complete(self):
        mission = self.env['space.mission']
        self.write({'state': 'complete'})
    
    def button_cancel(self):
        mission = self.env['space.mission']
        self.write({'state': 'cancel'})
