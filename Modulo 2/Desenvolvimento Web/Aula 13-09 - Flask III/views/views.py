from app import app
from flask import render_template

@app.route('/')
def index ():
    return render_template('index.html')

@app.route('/combinacoes')
def combinacoes():
    return render_template('combinacoes.html')

@app.route('/estoque.html')
def estoque():
    return render_template('estoque.html')

