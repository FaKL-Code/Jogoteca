from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)

@app.route('/home')
def home():
    return render_template('lista.html', titulo='Jogos')

app.run()
