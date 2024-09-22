from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/sayhello/<nombre>', methods=['GET'])
def say_hello(nombre):
    saludo = f"Hola, bienvenido! {nombre}"
    return jsonify({"saludo": saludo})

if __name__ == '__main__':
    app.run(debug=True)
