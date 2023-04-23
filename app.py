from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
    if request.method == "POST":
        peso = float(request.form['peso'])
        altura = float(request.form['altura'])
        indice = round ((peso/(altura/100*altura/100)), 3)

        return render_template('imc.html', peso=peso, altura=altura, indice=indice)
    
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)