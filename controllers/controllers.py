# -*- coding: utf-8 -*-
from odoo import http

# class OdooPackageAddon(http.Controller):
#     @http.route('/odoo_package_addon/odoo_package_addon/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/odoo_package_addon/odoo_package_addon/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('odoo_package_addon.listing', {
#             'root': '/odoo_package_addon/odoo_package_addon',
#             'objects': http.request.env['odoo_package_addon.odoo_package_addon'].search([]),
#         })

#     @http.route('/odoo_package_addon/odoo_package_addon/objects/<model("odoo_package_addon.odoo_package_addon"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('odoo_package_addon.object', {
#             'object': obj
#         })