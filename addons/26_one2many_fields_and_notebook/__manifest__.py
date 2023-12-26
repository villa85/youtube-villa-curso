{
    'name': 'Main Model with one2many MFH',
    'version': '14.0',
    'author': 'Yuniel Villalón',
    'maintainer': 'Yuniel Villalón',
    'license': 'AGPL-3',
    'category': 'Extra Tools',
    'summary': 'Main Model with one2many',
    'depends': ['base'],
    'data': [
            'security/ir.model.access.csv',
            'data/ir_sequence.xml',
            'views/main_model_view.xml',
            'reports/model_report.xml',
            'reports/reports.xml',
            ],
    'images': ['static/description/banner.jpg'],
}