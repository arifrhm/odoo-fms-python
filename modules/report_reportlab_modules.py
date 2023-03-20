from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph

# Define data for each report
vehicle_summary_data = [    ['Vehicle Make', 'Vehicle Model', 'Vehicle Year', 'License Plate', 'Fuel Type', 'Vehicle Type',     'Current Odometer Reading', 'Total Maintenance Cost', 'Total Fuel Cost', 'Total Distance Traveled',     'Average Fuel Efficiency'],
    ['Toyota', 'Corolla', '2018', 'ABC123', 'Gasoline', 'Car', '50,000', '$2,500', '$1,000', '100,000', '25 MPG'],
    ['Ford', 'F-150', '2020', 'DEF456', 'Diesel', 'Truck', '75,000', '$3,000', '$2,000', '150,000', '20 MPG']
]

maintenance_data = [    ['Vehicle Make', 'Vehicle Model', 'Vehicle Year', 'License Plate', 'Maintenance Date', 'Maintenance Type',     'Maintenance Cost', 'Mileage at Maintenance'],
    ['Toyota', 'Corolla', '2018', 'ABC123', '2022-01-01', 'Oil Change', '$50', '55,000'],
    ['Ford', 'F-150', '2020', 'DEF456', '2022-02-15', 'Tire Rotation', '$100', '80,000']
]

fuel_usage_data = [    ['Vehicle Make', 'Vehicle Model', 'Vehicle Year', 'License Plate', 'Fuel Purchase Date', 'Fuel Amount',     'Fuel Unit Price', 'Fuel Total Price', 'Mileage at Fuel Purchase'],
    ['Toyota', 'Corolla', '2018', 'ABC123', '2022-03-01', '10 gallons', '$2.50/gallon', '$25', '90,000'],
    ['Ford', 'F-150', '2020', 'DEF456', '2022-03-15', '15 gallons', '$3.00/gallon', '$45', '100,000']
]

trip_log_data = [    ['Vehicle Make', 'Vehicle Model', 'Vehicle Year', 'License Plate', 'Trip Date', 'Start Location',     'End Location', 'Distance Traveled', 'Driver Name', 'Driver Contact Details'],
    ['Toyota', 'Corolla', '2018', 'ABC123', '2022-03-01', 'New York', 'Washington D.C.', '225 miles', 'John Doe', '555-1234'],
    ['Ford', 'F-150', '2020', 'DEF456', '2022-03-15', 'Los Angeles', 'San Francisco', '400 miles', 'Jane Smith', '555-5678']
]

# Define functions to create tables and add styles
def create_table(data):
    table = Table(data)
    table_style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.gray),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, 0), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 14),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('TEXTCOLOR', (0, 1), (-1, -1), colors.black),
        ('ALIGN', (0, 1), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 1), (-1, -1), 12),
        ('BOTTOMPADDING', (0, 1), (-1, -1), 6),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
        ])
    table.setStyle(table_style)
    return table

def generate_report(template_filename, data, title):
    # Create the report object
    report = SimpleDocTemplate(template_filename)
    # Create the title and add it to the report
    report_title = Paragraph(title, styles['Title'])
    report.append(report_title)

    # Create the table and add it to the report
    report_table = create_table(data)
    report.append(report_table)

    # Close the report
    report.build()

if __name__ == "__main__":
    generate_report('vehicle_summary_report.pdf', vehicle_summary_data, 'Vehicle Summary Report')
    generate_report('maintenance_report.pdf', maintenance_data, 'Maintenance Report')
    generate_report('fuel_usage_report.pdf', fuel_usage_data, 'Fuel Usage Report')
    generate_report('trip_log_report.pdf', trip_log_data, 'Trip Log Report')