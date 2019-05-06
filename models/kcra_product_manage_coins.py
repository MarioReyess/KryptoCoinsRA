# -*- coding: utf-8 -*-

from odoo import models, fields, api

class kcra__product_manage(models.Model):
    _name = 'kcra__product_manage.kcra__product_manage'

    name = fields.Char(string="Nom moneda")
    pages = fields.Float(string="Valor")