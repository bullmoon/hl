from waitress import serve
from app import create_app  # Замените `app` на имя вашего Flask-приложения
app = create_app()

if __name__ == '__main__':
    serve(app, host='127.0.0.1', port=8000)