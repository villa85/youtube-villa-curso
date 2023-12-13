import jinja2
from odoo import http
from odoo.http import request
from odoo.exceptions import UserError
from odoo import models, fields, _
import werkzeug
import werkzeug.utils
import base64

import logging
_logger = logging.getLogger(__name__)

loader = jinja2.PackageLoader('odoo.addons.37_search_customers', 'views')
env = jinja2.Environment(loader=loader, autoescape=True)

class SearchCustomer(http.Controller):

    @http.route('/public/customer', methods=['GET'],  cors='*', auth='public')
    def get_home(self, **kwargs):
        my_current_url = request.session.get('my_current_url')
        user = kwargs.get('user_id')
        company = http.request.env['res.company'].sudo().search([], limit=1)
        return env.get_template('home.html').render({
                'csrf_token': http.request.csrf_token(),
                'vat_id': False,
            })

    # http://localhost:8069/public/customer/1234567890
    @http.route('/public/customer/<vat>', methods=['GET'],  cors='*', auth='public')
    def get_form(self, **kwargs):
        # url from config_parameter web.base.url
        web_base_url = http.request.env['ir.config_parameter'].sudo().get_param('web.base.url') + '/public/customer/'
        user = kwargs.get('user_id')

        vat_id = http.request.env['res.partner'].sudo().search([
            ('vat', '=', kwargs.get('vat')),
            ('active', '=', True),
        ], limit=1)

        _logger.info('vat_id: %s', vat_id)

        if vat_id:
            return env.get_template('home.html').render({
                'csrf_token': http.request.csrf_token(),
                'vat_id': vat_id,
                'web_base_url': web_base_url,
                'vat_img': vat_id.image_512 and 'data:image/png;base64,%s' % vat_id.image_512.decode()
            })

        else:
            return env.get_template('home.html').render({
                    'csrf_token': http.request.csrf_token(),
                    'vat_id': False,
                    'web_base_url': web_base_url,
                })
