from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("index.html")

@app.route("/sobre")
def sobre():
    return render_template("sobre.html")

@app.route("/busca")
def busca():
    # Certifique-se de ter um arquivo 'busca.html' na pasta templates
    return render_template("busca.html") 

@app.route("/contato")
def contato():
    # Certifique-se de ter um arquivo 'contato.html' na pasta templates
    return render_template("contato.html")

if __name__ == "__main__":
    app.run(debug=True)