from odoo import models, fields, api

class Vehicle(models.Model):
    _name = 'fleet.vehicle'
    _description = 'Vehicle'

    # Define vehicle fields
    make = fields.Char(required=True)
    model = fields.Char(required=True)
    year = fields.Integer(required=True)
    license_plate = fields.Char(required=True)
    fuel_type = fields.Selection([('petrol', 'Petrol'), ('diesel', 'Diesel'), ('electric', 'Electric')], required=True)
    odometer_reading = fields.Float()
    color = fields.Char()
    vin = fields.Char(string='VIN Number')
    registration_date = fields.Date()

    # Define vehicle relationships
    type_id = fields.Many2one('fleet.vehicle.type', string='Vehicle Type')
    maintenance_ids = fields.One2many('fleet.vehicle.maintenance', 'vehicle_id', string='Maintenance Logs')

    # Define mileage calculation method
    @api.multi
    def calculate_mileage(self):
        # Calculate mileage based on the last two odometer readings
        last_reading = self.env['fleet.vehicle.odometer'].search([('vehicle_id', '=', self.id)], order='date desc', limit=1)
        second_last_reading = self.env['fleet.vehicle.odometer'].search([('vehicle_id', '=', self.id), ('id', '<', last_reading.id)], order='date desc', limit=1)
        if last_reading and second_last_reading:
            return last_reading.value - second_last_reading.value
        else:
            return 0

    # Define maintenance task creation method
    @api.multi
    def create_maintenance_task(self, name, description, cost):
        # Create a new maintenance task for the vehicle
        maintenance = self.env['fleet.vehicle.maintenance'].create({
            'name': name,
            'description': description,
            'cost': cost,
            'vehicle_id': self.id
        })
        return maintenance