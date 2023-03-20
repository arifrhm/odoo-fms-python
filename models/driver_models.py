from odoo import models, fields, api

class Driver(models.Model):
    _name = 'fleet.driver'
    _description = 'Driver'

    # Define driver fields
    name = fields.Char(required=True)
    email = fields.Char()
    phone = fields.Char()
    license_number = fields.Char(required=True)
    license_expiry = fields.Date()
    address = fields.Char()
    date_of_birth = fields.Date()
    driving_history = fields.Text()

    # Define driver relationships
    vehicle_ids = fields.Many2many('fleet.vehicle', string='Vehicles')

    # Define driver performance tracking method
    @api.multi
    def track_performance(self):
        # Calculate the average score for the driver based on all the maintenance logs for their assigned vehicles
        scores = [maintenance.score for vehicle in self.vehicle_ids for maintenance in vehicle.maintenance_ids if maintenance.score]
        if scores:
            return sum(scores) / len(scores)
        else:
            return 0

    # Define vehicle assignment method
    @api.multi
    def assign_to_vehicle(self, vehicle):
        # Assign the driver to the specified vehicle
        self.vehicle_ids = [(4, vehicle.id)]