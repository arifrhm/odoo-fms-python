from odoo import models, fields, api

class VehicleType(models.Model):
    _name = 'fleet.vehicle.type'
    _description = 'Vehicle Type'

    # Define vehicle type fields
    name = fields.Char(required=True)
    description = fields.Text()
    capacity = fields.Integer()
    max_load = fields.Float()

    # Define vehicle type relationships
    vehicle_ids = fields.One2many('fleet.vehicle', 'type_id', string='Vehicles')

    # Define fuel efficiency calculation method
    @api.multi
    def calculate_fuel_efficiency(self):
        # Calculate the average fuel consumption for all vehicles of this type
        total_fuel = sum(vehicle.fuel_logs.mapped('quantity') for vehicle in self.vehicle_ids)
        total_distance = sum(vehicle.fuel_logs.mapped('distance') for vehicle in self.vehicle_ids)
        if total_fuel and total_distance:
            return total_distance / total_fuel
        else:
            return 0

    # Define performance report generation method
    @api.multi
    def generate_performance_report(self):
        # Generate a report on the performance of all vehicles of this type
        report = 'Performance report for vehicle type %s:\n' % self.name
        for vehicle in self.vehicle_ids:
            report += 'Vehicle %s:\n' % vehicle.name
            report += ' - Odometer reading: %s\n' % vehicle.odometer_reading
            report += ' - Fuel consumption: %s\n' % vehicle.calculate_fuel_efficiency()
            report += ' - Maintenance logs: %s\n' % ', '.join(log.name for log in vehicle.maintenance_ids)
            report += '\n'
        return report