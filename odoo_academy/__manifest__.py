# -*- coding: utf-8 -*-

{
    'name': 'Odoo Academy',
    
    'summary': """Academy app to manage Training""",
    
    'description':"""
        Academy Module to manage Training:
        - Courses
        - Sessions
        - Attendees    
    """,
    
    'author': 'Teko',
    
    'website': 'cube48.de',
    
    'category': 'Training',
    'version': '0.1',
    
    'depends': ['base'],
    
    'data': [
        'security/academy_security.xml',
        'security/ir.model.access.csv',
        'views/academy_menuitems.xml',
        'views/course_views.xml',
        'views/session_views.xml',
        
    ],
    
    'demo': [
        'demo/academy_demo.xml',
        
    ],
    
}