{
    'name': 'Create Invoice and Payment MFH',
    'version': '17.0',
    'author': 'Yuniel Villalón',
    'maintainer': 'Yuniel Villalón',
    'license': 'AGPL-3',
    'category': 'Extra Tools',
    'summary': 'Create Invoice and Payment.',
    'depends': ['base','account'],
    'data': [
            'security/ir.model.access.csv',
            'security/security.xml',
            'data/ir_sequence.xml',
            'views/create_invoice_view.xml',
            ],
    'images': ['static/description/banner.jpg'],
}