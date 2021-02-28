# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Dato(models.Model):
    _name = 'seguros.servicio'
    idservicio = fields.Integer('Id servicio', required=True)
    descripcion = fields.Char('Descripcion', required=True)
    precio = fields.Float('Precio', required=True)

    def name_get(self):
        res = []
        for record in self:
            name = record.descripcion
            res.append((record.id, name))
        return res
