from flask import render_template
from . import equipment

@equipment.route('/equipment')
def equipment_index():
    return render_template('equipment.html')

@equipment.route('/equipment/details')
def equipment_details():
    return render_template('details.html')
