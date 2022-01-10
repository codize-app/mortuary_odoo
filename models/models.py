# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ResPartner(models.Model):
    _inherit = 'res.partner'

    death_certificate = fields.Binary('Acta de Defunción')
    identification = fields.Binary('DNI')
