# -*- coding: utf-8 -*-
from odoo import api, fields, models

class EjPet(models.Model):
    _inherit = 'ej.pet'

    skin = fields.Char(string="Skin", size=20, default="Blue")
    walk = fields.Char(string="Walk")

    is_prety_name = fields.Boolean(string="Is prety name", compute="_compute_prety_name")

    dateb = fields.Date("Date", default = fields.Date.today)

    @api.depends("skin", "name")
    def _compute_prety_name(self):
        for record in self:
            record.is_prety_name = record.skin == "Blue"