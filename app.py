from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hola, soy [TU NOMBRE] y hoy aprendí a hacer una app"

if __name__ == "__main__":
    app.run()
