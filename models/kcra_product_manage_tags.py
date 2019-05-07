# -*- coding: utf-8 -*-

from odoo import models, fields, api


class kcra__product_manage_tags(models.Model):
    _name = 'kcra__product_manage_tags'

    name = fields.Char(string="Nom etiqueta")
    # coins_id = fields.One2many("kcra__product_manage_coins", "tags_id", string="Coins")
