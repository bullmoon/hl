from flask import render_template
from . import military

@military.route('/<category>')
def military_index(category):
    valid_categories = ["emission", "susceptebility"]
    if category in valid_categories:
        return render_template('military.html', category=category)
    else:
        return render_template('military.html', category=None)

@military.route('/')
def military_default():
    return render_template('military.html')

@military.route('/emission/<test>')
def military_emission(test):
    valid_tests = ["ce102", "re102", "re102v2"]
    if test in valid_tests:
        return render_template('military_emission_test.html', test=test)
    else:
        return render_template('military.html', test=None)

@military.route('/susceptebility/<test>')
def military_susceptebility(test):
    valid_tests = ["rs103"]
    if test in valid_tests:
        return render_template('military_susceptebility_test.html', test=test)
    else:
        return render_template('military.html', test=None)