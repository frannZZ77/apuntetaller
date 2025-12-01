from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('inicio.html')

@app.route('/flask')
def flask_page():
    return render_template('flask.html')

@app.route('/git')
def git():
    return render_template('git.html')

@app.route('/arduino')
def arduino():
    return render_template('arduino.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)