from odoo import  http
from odoo.http import request
import json


class POSDiscountAuth(http.Controller):
    @http.route(['/pos_discount_auth_code'], type="json", auth='public', methods=['POST'], csrf=False)
    def check_auth_code(self):
        auth_code = request.env['ir.config_parameter'].sudo(
        ).get_param('pos_discount_auth.authorized_code')

        data = json.loads(request.httprequest.data)
        cashier_auth_code = data['params']["cashier_auth_code"]

        return {'authenticated': auth_code == cashier_auth_code}

