# -*- encoding: utf-8 -*-

import logging

from openerp import http
from openerp.http import request

_logger = logging.getLogger(__name__)


class supplier_create(http.Controller):
	@http.route('/supplier/create', type='json', auth="none", jsonrpckey=True)
	def create_supplier(self, **post):
		user = request.jsonrpckey['user']
		env = request.env(user=user.id)

		supplier = env['supplier.test']

        payload = {
            'supplier_id': supplier_id.id,
            'supplier_name': supplier_name,
            'supplier_code': supplier_code,
      
        }
        new_entries = supplier.create(payload)
		
		