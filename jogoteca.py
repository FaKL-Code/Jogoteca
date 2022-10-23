from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)

@app.route('/home')
def home():
    lista = ['Super Mario', 'Zelda', 'Donkey Kong', 'Mortal Kombat']
    return render_template('lista.html', titulo='Jogos', jogos=lista)

app.run()
