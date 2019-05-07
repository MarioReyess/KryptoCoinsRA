# -*- coding: utf-8 -*-

from odoo import models, fields, api


class kcra__product_manage(models.Model):
    _name = 'kcra__product_manage.kcra__product_manage_coins'

    name = fields.Char(string="Nom moneda")
    price = fields.Float(string="Preu")
    tags_id = fields.Many2one("kcra__product_manage_tags", string="Etiqueta")
