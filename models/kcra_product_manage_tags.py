# -*- coding: utf-8 -*-

from odoo import models, fields, api


class kcra__product_manage(models.Model):
    _name = 'kcra__product_manage.kcra__product_manage_tags'

    name = fields.Char(string="Nom etiqueta")
    coins_id = fields.Many2one("kcra__product_manage_coins", string="Coins")

