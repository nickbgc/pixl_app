from flask import render_template
from app import app
from app.visualization import get_visualization

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    plot = get_visualization()
    return render_template('dashboard.html', plot=plot)
