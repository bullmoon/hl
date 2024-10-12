from flask import Blueprint

calculators = Blueprint(
    'calculators', 
    __name__,
    static_folder='static',  # Route to static
    template_folder='templates'  # Route to templates
)

from . import routes
