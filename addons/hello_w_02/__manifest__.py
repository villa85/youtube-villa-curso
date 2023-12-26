##############################################################################
#
#    OpenERP, Open Source Management Solution
#    This module copyright (C) 2023 Yuniel Villalón Rosales
#
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
    'name': 'Hello W2',
    'version': '14.0',
    'author': 'Yuniel Villalón Rosales',
    'maintainer': 'Yuniel Villalón Rosales',
    'license': 'AGPL-3',
    'category': 'Extra Tools',
    'summary': 'Short summary.',
    'depends': ['base', 'hello_w'],
    'data': [
        'views/view.xml',
        "data/pet_data.xml",
    ],
    'images': ['static/description/banner.png'],
}
