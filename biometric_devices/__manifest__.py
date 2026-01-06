{
    'name': "Biometric Devices",
    'summary': """Integrating Biometric Device  With HR""",
    'description': """
    
    """,

    'author': "Tarek Ashry",
    'company': 'Softobia',
    'website': 'https://www.softobia.com',

    'category': 'Human Resources',
    'version': '19.0.1.0',

    'depends': ['base_setup', 'hr', 'hr_attendance'],

    'data': [
        'security/ir.model.access.csv',
        'views/biometric_device_views.xml',
        'views/biometric_attendance_views.xml',
        'views/biometric_menus.xml',
    ],
    'license': 'LGPL-3',
}
