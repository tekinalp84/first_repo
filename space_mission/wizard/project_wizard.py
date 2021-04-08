# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ProjectWizard(models.TransientModel):
    _name = 'space.project.wizard'
    _description = 'Wizard: Add mission projects on the fly'
    
    def _default_mission(self):
        return self.env['space.mission'].browse(self._context.get('active_id'))
    
    
    mission_id = fields.Many2one(comodel_name='space.mission',
                                string='Mission',
                                required=True,
                                default=_default_mission)
    
    name = fields.Char(string='Project Name')
    
    
    def create_projects(self):
        
        project_id= self.env['project.project'].create({
            'mission_id': self.mission_id.id,
            'name': self.name
        })