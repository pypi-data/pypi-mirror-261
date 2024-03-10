# __init__.py in your_package directory

from .app import app

def run():
    app.run(debug=True)
