from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def calculatrice():
    resultat = None
    if request.method == 'POST':
        try:
            a = float(request.form['a'])
            b = float(request.form['b'])
            operation = request.form['operation']
            if operation == 'add':
                resultat = a + b
            elif operation == 'sub':
                resultat = a - b
            elif operation == 'mul':
                resultat = a * b
            elif operation == 'div':
                resultat = a / b if b != 0 else 'Erreur : division par zéro'
        except ValueError:
            resultat = 'Erreur : entrez des nombres valides'
    return render_template('index.html', resultat=resultat)

if __name__ == '__main__':
    app.run(debug=True)
