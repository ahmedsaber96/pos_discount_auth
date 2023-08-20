# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import models, fields, api
from odoo.exceptions import UserError


class PosConfig(models.TransientModel):
    _inherit = "res.config.settings"

    authorized_code = fields.Char('Authorized Code', size=4, help=u'Four digits code. It grants access to the POS salesman to apply discounts from POS UI.', config_parameter="pos_discount_auth.authorized_code")

    @api.constrains('authorized_code')
    def check_pos_discount_authorization_code(self):
        for record in self:
            if len(record.authorized_code) < 4:
                raise UserError(u'Authorized code must be a 4 digits number.')