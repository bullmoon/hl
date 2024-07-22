from flask import current_app, send_from_directory

@current_app.route('/favicon.ico')
def favicon():
    print("Favicon requested")
    return send_from_directory(current_app.static_folder, 'favicon.ico')
