# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions

class Chef(models.Model):
    _name = 'vezo.chef'
    _rec_name = 'chef_name'

    chef_image = fields.Binary('Ảnh')
    chef_name = fields.Char('Tên')
    chef_address = fields.Char('Địa chỉ')
    chef_telephone = fields.Char('Số điện thoại')
    chef_email = fields.Char('Email')


    @api.constrains('chef_name')
    def _chef_name_validate(self):
        for chef in self:
            if len(chef.chef_name.strip()) < 1:
                raise exceptions.ValidationError(u'Không được để trống tên Chef')
