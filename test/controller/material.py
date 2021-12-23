# -*- coding: utf-8 -*-
from openerp import http
from openerp.http import request
import json

class material_update(http.Controller):
    @http.route('/material/create', type='json', auth="none", jsonrpckey=True)
    def create_supplier(self, **post):
        user = request.jsonrpckey['user']
        env = request.env(user=user.id)

        material = env['material.test']

        payload = {
            'material_code': material_code,
            'material_name': material_name,
            'material_type': material_type,
            'material_buy_price':material_buy_price,
            'supplier_id': supplier_id.id  
        }
        update = material.create(payload)
        

class material_get(http.Controller):
    
    @http.route('/material/view', type='http', auth='public')
    def index(self, **kw):
        result = []
        data = request.env['material.test'].search([material_buy_price > 100])
        for val in data:
            result.append({
                'material_code': val.material_code,
                'material_name': val.material_name,
                'material_type': val.material_type,
                'material_buy_price': val.material_buy_price,
                'supplier_id': val.supplier_id.id,
                })
        res = {'material': result}
        return str(json.dumps(res))
        

