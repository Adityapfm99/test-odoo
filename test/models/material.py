# -*- coding: utf-8 -*-

from openerp import models, fields, api

class supplier(models.Model):
    _name = 'supplier.test'

    supplier_id = fields.Many2one('material.test', string='Supplier Id')
    supplier_code = fields.Char('Supplier Code')
    supplier_name = fields.Char('Supplier Name')
    


class material(models.Model):
    _name = 'material.test'

    material_code = fields.Char('Material Code')
    material_name = fields.Char('Material Name')
    material_type = = fields.Selection([
        ('fabric', 'Fabric'),
        ('jens', 'Jeans'),
        ('cotton', 'Cotton')], string='Material type',
        default='fabric', required=True)
    material_buy_price = fields.Float(string='Material Buy Price')
    supplier_id = fields.One2many(
        'supplier.test', string='Related Supplier',
        track_visibility='onchange')
