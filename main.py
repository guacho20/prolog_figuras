from flask import Flask, request, render_template, flash, redirect, url_for
from pyswip import Prolog

# Application initializations
app = Flask(__name__)

# settings como va ir protegida la session
app.secret_key = "mysecretkey"

# prolog
prolog = Prolog()
prolog.consult("figuras.pl", True)

@app.route("/")
def Index():
    return render_template("index.html", data=[])

@app.route("/reset")
def reset():
    return redirect(url_for("Index"))

@app.route("/search", methods=["POST"])
def search():
    if request.method == "POST":
        radio = request.form["radio"]
        lado = request.form["lado"]
        angulo_recto = request.form["angulo_recto"]
        print(radio, lado,angulo_recto)

        figura = list(prolog.query("clasificar_figura(F," + radio + "," + lado + ","+ angulo_recto +")"))
        print(figura[0]['F'])
        flash(figura[0]['F'])

        return redirect(url_for("Index"))


# starting the app
if __name__ == "__main__":
    app.run(port=4000, debug=True)
