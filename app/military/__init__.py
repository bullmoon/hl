from flask import Blueprint

military = Blueprint(
    'military', 
    __name__,
    static_folder='static',  # Путь к статическим файлам
    template_folder='templates'  # Путь к шаблонам
)

from . import routes
