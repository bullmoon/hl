from app import create_app

app = create_app()

# Set default Gunicorn bind if no --bind option is specified
import os
if "GUNICORN_CMD_ARGS" not in os.environ:
    os.environ["GUNICORN_CMD_ARGS"] = "--bind=127.0.0.1:8080"
