# -*- coding: utf-8 -*-
from odoo import http

# class KcraProductManage(http.Controller):
#     @http.route('/kcra__product_manage/kcra__product_manage/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/kcra__product_manage/kcra__product_manage/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('kcra__product_manage.listing', {
#             'root': '/kcra__product_manage/kcra__product_manage',
#             'objects': http.request.env['kcra__product_manage.kcra__product_manage'].search([]),
#         })

#     @http.route('/kcra__product_manage/kcra__product_manage/objects/<model("kcra__product_manage.kcra__product_manage"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('kcra__product_manage.object', {
#             'object': obj
#         })