from flask import render_template
from . import automotive

@automotive.route('/<category>')
def automotive_index(category):
    valid_categories = ["emission", "immunity"]
    if category in valid_categories:
        return render_template('automotive.html', category=category)
    else:
        return render_template('automotive.html', category=None)

@automotive.route('/')
def automotive_default():
    return render_template('automotive.html')

@automotive.route('/immunity/<test>')
def automotive_immunity(test):
    valid_tests = ["11452-4", "11452-2", "7637-2"]
    if test in valid_tests:
        return render_template('automotive_immunity_test.html', test=test)
    else:
        return render_template('automotive.html', test=None)

@automotive.route('/emission/<test>')
def automotive_emission(test):
    valid_tests = ["r10", "tl81000", "cispr25"]
    if test in valid_tests:
        return render_template('automotive_emission_test.html', test=test)
    else:
        return render_template('automotive.html', test=None)
