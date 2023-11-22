#-*- coding: utf-8 -*-

from odoo import fields, models, api, _
import base64
from io import BytesIO
from odoo.tools.misc import xlwt


class PartnerExportExcel(models.TransientModel):
    _name = "partner.export.excel"
    _description = "Export Partner Excel"

    company_type = fields.Selection([('person', 'Individual'), ('company', 'Company'),('all','All')], string='Company Type', default='all')

    def export_partner_excel(self):
        domain = []
        if self.company_type != 'all':
            domain.append(('type', '=', self.company_type))
        partners = self.env['res.partner'].search(domain)
        return self._helper_export_partner_excel(partners)

    def _helper_export_partner_excel(self,partners):
        workbook = xlwt.Workbook(encoding="utf-8")
        worksheet = workbook.add_sheet(_("Partner"))
        file_name = _("Partners")
        style_border_table_top = xlwt.easyxf(
            'borders: left thin, right thin, top thin, bottom thin; font: bold on;')
        style_border_table_details = xlwt.easyxf('borders: bottom thin;')
        style_border_table_details_red = xlwt.easyxf('borders: bottom thin; font: colour red, bold True;')

        worksheet.write(0, 0, _("Vat"), style_border_table_top)
        worksheet.write_merge(0, 0, 1, 3, _("Partner"), style_border_table_top)
        worksheet.write(0, 4, _("Phone"), style_border_table_top)
        worksheet.write(0, 5, _("Email"), style_border_table_top)

        row = 1
        for partner in partners:
            style = style_border_table_details
            if not partner.vat:
                style = style_border_table_details_red
            worksheet.write(row, 0, partner.vat or '', style)
            worksheet.write_merge(row, row, 1, 3, str(partner.name), style)
            worksheet.write(row, 4, partner.phone, style)
            worksheet.write(row, 5, partner.email, style)
            row += 1

        fp = BytesIO()
        workbook.save(fp)
        fp.seek(0)
        data = fp.read()
        fp.close()
        data_b64 = base64.encodebytes(data)
        doc = self.env['ir.attachment'].create({
            'name': '%s.xls' % (file_name),
            'datas': data_b64,
        })
        return {
            'type': "ir.actions.act_url",
            'url': "web/content/?model=ir.attachment&id=" + str(
                doc.id) + "&filename_field=name&field=datas&download=true&filename=" + str(doc.name),
            'no_destroy': False,
        }