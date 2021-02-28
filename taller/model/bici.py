#-*- coding: utf-8 -*-

from odoo import models, fields, api

class Dato(models.Model):
	_name = 'taller.bici'
	idbici = fields.Char('Id bici', required=True)
	marca = fields.Char('marca',required=True)
	telefono = fields.Integer('Telefono',required=True)
	cliente = fields.Many2one('taller.cliente','Cliente')
	servicio = fields.Many2many('taller.servicio',"many2many_default")


