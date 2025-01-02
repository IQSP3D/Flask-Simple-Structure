from flask import render_template
from app import create_app

app = create_app()

@app.route('/')
def home():
    return render_template('base.html')
