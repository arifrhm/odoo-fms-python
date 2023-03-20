from flask import Flask, request, jsonify
from flask_odoo import Odoo
from flask_restful import Api, Resource
from flask_login import login_required

app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecretkey'
app.config['ODOO_SERVER'] = 'http://localhost:8069'
app.config['ODOO_DATABASE'] = 'mydatabase'
app.config['ODOO_USERNAME'] = 'admin'
app.config['ODOO_PASSWORD'] = 'password'

odoo = Odoo(app)
api = Api(app)

class Vehicle(Resource):
    @login_required
    def get(self, id):
        Vehicle = odoo.env['fleet.vehicle']
        vehicle = Vehicle.browse(int(id))
        return {
            'id': vehicle.id,
            'make': vehicle.make,
            'model': vehicle.model,
            'year': vehicle.year,
            'license_plate': vehicle.license_plate,
            'fuel_type': vehicle.fuel_type,
            'vehicle_type': vehicle.vehicle_type,
            'odometer_reading': vehicle.odometer,
            'driver_id': vehicle.driver_id.id if vehicle.driver_id else None
        }

class VehicleList(Resource):
    @login_required
    def get(self):
        Vehicle = odoo.env['fleet.vehicle']
        vehicles = Vehicle.search_read([], ['id', 'make', 'model', 'year', 'license_plate'])
        return jsonify(vehicles)

api.add_resource(Vehicle, '/vehicles/<int:id>')
api.add_resource(VehicleList, '/vehicles')

if __name__ == '__main__':
    app.run(debug=True)
