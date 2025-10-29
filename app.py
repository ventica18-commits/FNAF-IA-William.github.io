from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/enviar", methods=["POST"])
def enviar():
    mensaje = request.form["mensaje"]

    # Guarda el mensaje en un archivo .txt para entrenar después
    with open("mensajes.txt", "a", encoding="utf-8") as archivo:
        archivo.write(mensaje + "\n")

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)