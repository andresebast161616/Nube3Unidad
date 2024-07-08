from flask import Flask, render_template, request, redirect, url_for, flash
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Genera una clave secreta aleatoria

USERNAME = "AndreeFlores"
PASSWORD = "2017057494"

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    
    if username == USERNAME and password == PASSWORD:
        flash('Login correcto', 'success')
        return redirect(url_for('home'))
    else:
        flash('Login incorrecto', 'danger')
        return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
