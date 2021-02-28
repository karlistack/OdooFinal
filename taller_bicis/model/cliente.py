# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Dato(models.Model):
    _name = 'gestion_taller_bici.cliente'
    nombre = fields.Char('Nombre', required=True)
    dni = fields.Char('DNI', required=True)

    def name_get(self):
        res = []
        for record in self:
            name = record.nombre
            res.append((record.id, name))
        return res
