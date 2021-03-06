# -*- coding: utf-8 -*-

{
    'name': 'Space Mission',
    
    'summary': """Help Odoo get to the Moon""",
    
    'description':"""
    Odoo Inc is trying to visit the Moon
    This app will help to organize the logistics
    """,
    
    'author': 'Onur Tekinalp',
    
    'website': 'https://cube48.de',
    
    'version': '0.1',
    
    'category': 'Logistics',
    
    'depends': ['project','website'],
    
    'data':[
        'security/space_mission_security.xml',
        'security/ir.model.access.csv',
        'views/space_mission_menuitems.xml',
        'views/spaceship_views.xml',
        'views/mission_views.xml',
        'views/project_views_inherit.xml',
        'wizard/project_wizard_views.xml',
        'report/spaceship_report.xml',
        'report/spaceship_report_template.xml',
        'views/space_web_templates.xml',
        
        
    ],
    
    'demo': [
        'demo/space_mission_demo.xml',
        
    ],
    
    
}