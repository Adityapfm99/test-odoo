
from openerp import models, fields, api

class supplier(models.Model):
    _name = 'supplier.test'

    supplier_id = fields.Many2one('material.test', string='Supplier Id')
    supplier_code = fields.Char('Supplier Code')
    supplier_name = fields.Char('Supplier Name')
    