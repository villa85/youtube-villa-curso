##############################################################################
#
#    OpenERP, Open Source Management Solution
#    This module copyright (C) 2018 Yuniel Villalón Rosales
#    (<http://www.marlonfalcon.com>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': 'Hello W',
    'version': '16.0.1.0.0',
    'author': 'Yuniel Villalón Rosales',
    'maintainer': 'Yuniel Villalón Rosales',
    'license': 'AGPL-3',
    'category': 'Extra Tools',
    'summary': 'Short summary.',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/view.xml',
        'data/ir_sequence.xml',
    ],
    'images': ['static/description/banner.png'],
}
