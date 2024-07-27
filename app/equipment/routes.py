from flask import render_template
from . import equipment

@equipment.route('/')
def equipment_index():
    return render_template('equipment.html')

@equipment.route('/equipment/<item>')
def equipment_list(item):
    valid_equipment = ["hl-1187"]
    if item in valid_equipment:
        return render_template('equipment.html', equipment=equipment)
    else:
        return render_template('equipment.html', equipment=None)