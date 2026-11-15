from odoo import models, fields


class FsmOrder(models.Model):
    _inherit = "expodo.fsm.order"

    license_plate = fields.Char(string="License Plate", index=True)
    vehicle_make = fields.Char(string="Make")
    vehicle_model = fields.Char(string="Model")
    vehicle_year = fields.Char(string="Year")
    mileage_in = fields.Integer(string="Mileage In")
    vin = fields.Char(string="VIN")
