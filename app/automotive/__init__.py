from flask import Blueprint

automotive = Blueprint(
    'automotive', 
    __name__,
    static_folder='static',  # Путь к статическим файлам
    template_folder='templates'  # Путь к шаблонам
)

from . import routes
