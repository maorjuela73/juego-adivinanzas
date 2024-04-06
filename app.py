from flask import Flask, request, render_template, session, redirect, url_for
import random

app = Flask(__name__)
app.secret_key = 'tu_clave_secreta_aqui'  # Necesaria para usar sesiones

@app.route('/', methods=['GET', 'POST'])
def index():
    if 'numero' not in session:
        session['numero'] = random.randint(1, 100)  # Generar un número aleatorio
        session['intentos'] = 0  # Contador de intentos

    mensaje = ''
    if request.method == 'POST':
        conjetura = int(request.form['conjetura'])
        session['intentos'] += 1
        if conjetura < session['numero']:
            mensaje = 'Más alto!'
        elif conjetura > session['numero']:
            mensaje = 'Más bajo!'
        else:
            return redirect(url_for('resultado'))

    return render_template('index.html', mensaje=mensaje)

@app.route('/resultado')
def resultado():
    intentos = session.pop('intentos')  # Obtener y limpiar el número de intentos
    session.pop('numero', None)  # Reiniciar el número para el próximo juego
    return render_template('resultado.html', intentos=intentos)

if __name__ == '__main__':
    app.run(debug=True)
