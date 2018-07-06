# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions

class Contact(models.Model):
    _name = 'vezo.contact'

    partner_name = fields.Char('Tên')
    partner_email = fields.Char('Email')
    address = fields.Char('Địa chỉ')
    partner_telephone = fields.Char('Số điện thoại')
    partner_note = fields.Text('Ghi chú')

    @api.constrains('partner_name')
    def _partner_name_validate(self):
        for partner in self:
            if len(partner.partner_name.strip()) < 1:
                raise exceptions.ValidationError(u'Không được để trống tên Partner')

class Partner(models.Model):
    _name = 'vezo.partner'
    _inherits = {'vezo.contact': 'partner'}

    partner_image = fields.Binary('Ảnh')
    # partner_name = fields.Char(related='vezo.contact.partner_name', inherited=True)
    partner_tax_code = fields.Char('Mã số thuế')
    partner_website = fields.Char('Website')
    partner_email = fields.Char('Email')
    partner_contact = fields.Many2one('vezo.contact', ondelete='cascade', string='Partner')
    partner_address = fields.Many2one('vezo.contact', ondelete='cascade', string='Address')

