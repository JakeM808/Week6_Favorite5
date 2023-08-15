from app import app
from flask import render_template

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/favorite_5')
def favorite_5():
    favorite_places = ['Fort Dauphine, Madagascar', 'Chang Mai, Thailand', 'Bali, Indonesia', 'Barcelona, Spain', 'Paris']
    return render_template('favorite_5.html', favorite_places=favorite_places)