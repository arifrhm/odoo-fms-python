from odoo import models, fields, api

class VehicleLogService(models.Model):
    _name = 'fleet.vehicle.log.services'
    _description = 'Vehicle Maintenance Log'

    # Define maintenance log fields
    date = fields.Date(required=True)
    type_id = fields.Many2one('fleet.service.type', required=True, string='Maintenance Type')
    cost = fields.Float()
    mileage = fields.Float()
    duration = fields.Float(string='Duration (hours)')
    severity = fields.Selection([('low', 'Low'), ('medium', 'Medium'), ('high', 'High')], string='Severity')

    # Define maintenance log relationships
    vehicle_id = fields.Many2one('fleet.vehicle', required=True, string='Vehicle')

    @api.depends('cost')
    def _compute_total_maintenance_cost(self):
        for record in self:
            record.vehicle_id.total_maintenance_cost += record.cost

    @api.model
    def get_maintenance_history_by_vehicle(self, vehicle_id):
        return self.search([('vehicle_id', '=', vehicle_id)])