{
    'name': 'Profiles',
    'version': '18.0.1.0.0',
    'category': 'Sales',
    'summary': 'Customer Profiles Management',
    'description': """
        Module for managing customer profiles:
        - Individual customer profiles
        - Company profiles
        - Customer information tracking
    """,
    'author': 'Your Company',
    'website': 'https://www.yourcompany.com',
    'depends': ['base', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/profile_views.xml',
    ],
    'application': True,
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
}