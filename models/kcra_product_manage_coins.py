# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions


class kcra__product_manage(models.Model):
    _name = 'kcra__product_manage_coins'

    name = fields.Char(string="Nom moneda")
    price = fields.Float(string="Preu")
    qty = fields.Integer(string="Quantitat")
    tags_id = fields.Many2many("kcra__product_manage_tags", string="Etiqueta")

    @api.onchange('name')
    def onchange_date(self):
        if self.name is '':
            raise exceptions.UserError("Nom de la Cripto Moneda Buit!")

    @api.onchange('price')
    def onchange_date(self):
        if self.name is 0:
            raise exceptions.UserError("Preu de la Cripto Moneda Buit!")


    @api.onchange('price')
    def onchange_date(self):
        if self.qty is 0:
            raise exceptions.UserError("Preu de la Cripto Moneda Buit!")
