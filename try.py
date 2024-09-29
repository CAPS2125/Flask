from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    columns = {
        "Ruta": "Ruta",
        "Hora_Ida": "Hora de Ida",
        "Hora_Llegada": "Hora de Llegada"
    }
    return render_template("hello_html.html", **columns)

if __name__ == '__main__':
    app.run()