from flask import render_template
import os
import json
from . import military

# Path to the JSON file (placed in static folder)
DATA_FILE = os.path.join(military.static_folder, 'data', 're102g_v1.json')

# Function to load JSON data
def load_data():
    """Loads data from the JSON file."""
    with open(DATA_FILE, 'r') as f:
        return json.load(f)

VALID_CATEGORIES = {
    "emission": ["ce102", "re102", "re102v2"],
    "susceptibility": ["rs103", "sec205", "cs101"]
}

@military.route('/')
def military_default():
    """Default route."""
    return render_template('military.html')

@military.route('/<category>')
def military_index(category):
    """Route for categories."""
    if category in VALID_CATEGORIES:
        return render_template('military.html', category=category)
    else:
        return render_template('military.html', category=None)
    
@military.route('/<category>/<test>')
def military_test(category, test):
    """Route for test in categories."""
    tests = VALID_CATEGORIES.get(category)
    if tests and test in tests:
        data = load_data()  # Load data from JSON
        template = f"military_{category}_test.html"
        # return render_template(template, test=test)
        return render_template(template, test=test, data=data)  # Pass JSON data to template
    else:
        return render_template('military.html', test=None)
