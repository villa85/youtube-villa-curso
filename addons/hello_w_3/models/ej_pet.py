# -*- coding: utf-8 -*-
from odoo import api, fields, models

class EjPet(models.Model):
    _name = 'ej.pet'
    name = fields.Char(string='name', required=True)
    code = fields.Char(string='code', dafault='New', readonly=1)
    age = fields.Integer(string='age')
    color = fields.Char(string='color')
    is_new = fields.Boolean(string='is_new', default=True)
    type = fields.Selection([('dog', 'Dog'),
                            ('cat', 'Cat'),
                            ('bird', 'Bird'),
                            ('fish', 'Fish'),
                            ('other', 'Other')], string='type', default="dog", required=False)

    @api.model
    def create(self, vals):
        if vals.get('code', "New") == "New":
            vals['code'] = self.env['ir.sequence'].next_by_code(
                'ej.pet') or "New"
        pet = super(EjPet, self).create(vals)
        return pet