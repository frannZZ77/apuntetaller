from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def Inicio():
    return render_template ('Inicio.html')


@app.route('/Arduino')
def Arduino():
    return render_template ('Arduino.html')


@app.route('/Flask')
def Flask():
    return render_template ('Flask.html')

@app.route('/Git')
def Git():
    return render_template ('Git.html')

if __name__=='__main__':
    app.run(debug=True)
    
    