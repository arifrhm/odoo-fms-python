from odoo import models, fields

class VehicleLogFuel(models.Model):
    _name = 'fleet.vehicle.log.fuel'
    _description = 'Vehicle Fuel Log'

    # Define fuel log fields
    date = fields.Date(required=True)
    amount = fields.Float(required=True)
    unit_price = fields.Float(required=True)
    total_price = fields.Float(required=True)
    mileage = fields.Float(required=True)

    # Define fuel log relationships
    vehicle_id = fields.Many2one('fleet.vehicle', required=True, string='Vehicle')