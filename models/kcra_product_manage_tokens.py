# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions

class kcra__product_manage_tokens(models.Model):
    _name = 'kcra__product_manage_tokens'

    name = fields.Char(string="Nom Token")
    price = fields.Float(string="Preu")
    qty = fields.Integer(string="Quantitat")
    tags_id = fields.Many2many("kcra__product_manage_tags", string="Etiqueta")
