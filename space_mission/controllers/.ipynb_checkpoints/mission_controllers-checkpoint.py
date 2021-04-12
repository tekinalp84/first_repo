# -*- coding: utf-8 -*-

from odoo import http

class Space(http.Controller):
    @http.route('/space/', auth='public', website=True, sitemap=True)
    def index(self, **kw):
        return "Space Mission Landing Page"
    
    @http.route('/space/missions', auth='public', website=True, sitemap=True)
    def missions(self, **kw):
        missions = http.request.env['space.mission'].search([])
        return http.request.render('space_mission.mission_website',{
            'missions':missions,
        })