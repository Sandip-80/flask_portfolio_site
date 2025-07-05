

# app.py
from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def home():
    """Renders the main portfolio page."""
    return render_template('index.html')

if __name__ == '__main__':
    # Run the Flask application in debug mode for development.
    # In a production environment, you would use a production-ready WSGI server.
    app.run(debug=True)
