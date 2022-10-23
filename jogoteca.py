from flask import Flask, render_template, request, redirect, session

class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console

app = Flask(__name__)

@app.route('/home')
def home():
    jogo_um = Jogo('God of War', 'Ação', 'PS4')
    jogo_dois = Jogo('Super Mario', 'Aventura', 'SNES')
    jogo_tres = Jogo('Pokemon', 'RPG', 'GBA')
    jogo_quatro = Jogo('Mortal Kombat', 'Luta', 'PS2')
    lista = [jogo_um, jogo_dois, jogo_tres, jogo_quatro]
    return render_template('lista.html', titulo='Jogos', jogos=lista)

app.run()

