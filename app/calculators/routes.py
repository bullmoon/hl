from flask import render_template
import os
import json
from . import calculators
import pandas as pd

# Path to the JSON file (placed in static folder)
DATA_FILE = os.path.join(calculators.static_folder, 'data', 'antenna_exp.json')

# Function to load JSON data
def load_data():
    """Loads data from the JSON file."""
    with open(DATA_FILE, 'r') as f:
        return json.load(f)

VALID_CATEGORIES = {
    "emission": ["ce102", "re102", "re102v2"],
    "susceptibility": ["rs103"]
}

@calculators.route('/')
def calculators_default():
    """Default route."""
    return render_template('calculators.html')

@calculators.route('/<category>')
def calculators_index(category):
    """Route for categories."""
    if category in VALID_CATEGORIES:
        return render_template('calculators.html', category=category)
    else:
        return render_template('calculators.html', category=None)
    
@calculators.route('/<category>/<test>')
def calculators_test(category, test):
    """Route for test in categories."""
    tests = VALID_CATEGORIES.get(category)
    if tests and test in tests:
        data = load_data()  # Load data from JSON
        template = f"calculators_{category}_test.html"
        # return render_template(template, test=test)
        return render_template(template, test=test, data=data)  # Pass JSON data to template
    else:
        return render_template('calculators.html', test=None)
