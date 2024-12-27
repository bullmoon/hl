# HL Project

Welcome to the **HL Project** repository! This project provides a modular Flask-based web application architecture, demonstrating how to structure a project using Flask Blueprints effectively.

## Features

- **Modular Design**: Separates different functionalities (e.g., `main`, `military`, `automotive`, `civilian`) using Flask Blueprints.
- **Customizable Structure**: Easily extendable for adding new sections or features.
- **Static Files Management**: Demonstrates handling of static files for multiple blueprints.
- **Dynamic Routing**: Includes examples of routing and URL generation using Flask's `url_for`.

---

## Project Structure

```plaintext
hl/
│
├── app/
│   ├── __init__.py                # Application factory for Flask
│   ├── main/                      # Main blueprint
│   │   ├── __init__.py            # Blueprint registration for main
│   │   ├── routes.py              # Routes for main
│   │   ├── static/                # Static files for main
│   │   │   ├── css/               # CSS files
│   │   │   ├── images/            # Images
│   │   ├── templates/             # Templates for main
│   │       ├── base.html          # Base template
│   │       ├── index.html         # Index template
│   ├── military/                  # Military blueprint
│   ├── automotive/                # Automotive blueprint
│   ├── civilian/                  # Civilian blueprint
│
├── requirements.txt               # Dependencies
├── config.py                      # Configuration file
├── run.py                         # Entry point for the application
└── README.md                      # This file
