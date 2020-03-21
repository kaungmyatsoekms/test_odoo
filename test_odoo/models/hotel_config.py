from odoo import models, fields, api

class HotelConfig(models.Model):

    _name = 'hotel.config'
    _description = 'hotel.config'

    name = fields.Char()
    code = fields.Char()