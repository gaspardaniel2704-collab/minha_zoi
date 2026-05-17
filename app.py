from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
SENHA = "Alzira2405"

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form['senha'] == SENHA:
            return redirect(url_for('pagina1'))
    return render_template('login.html')


@app.route('/pagina1')
def pagina1():
    return render_template('pagina1.html')


@app.route('/pagina2')
def pagina2():
    return render_template('pagina2.html')


@app.route('/pagina3')
def pagina3():
    return render_template('pagina3.html')


@app.route('/pagina4')
def pagina4():
    return render_template('pagina4.html')


@app.route('/pagina5')
def pagina5():
    return render_template('pagina5.html')


@app.route('/forca')
def forca():
    return render_template('forca.html')


@app.route('/final')
def final():
    return render_template('final.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)