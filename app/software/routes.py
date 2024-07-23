from flask import render_template, url_for
from . import software

@software.route('/')
def index():
    return render_template('software.html')

@software.route('/about')
def about():
    return render_template('about.html')
