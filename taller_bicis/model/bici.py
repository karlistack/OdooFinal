#-*- coding: utf-8 -*-

from odoo import models, fields, api

class Dato(models.Model):
	_name = 'gestion.bici'
	idservicio = fields.Char('Id bici', required=True)
	empresa = fields.Char('Empresa',required=True)
	telefono = fields.Integer('Telefono',required=True)
	cliente = fields.Many2one('gestion.cliente','Cliente')
	bici = fields.Many2many('gestion.bici',"many2many_default")


