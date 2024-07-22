from flask import render_template
from . import military

@military.route('/')
def military_index():
    return render_template('military.html')

@military.route('/military/details')
def automotive_details():
    return render_template('details.html')
