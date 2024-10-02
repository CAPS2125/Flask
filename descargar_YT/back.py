from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def lobby():
    return render_template("estructuras.html")

if __name__ == '__main__':
    app.run()