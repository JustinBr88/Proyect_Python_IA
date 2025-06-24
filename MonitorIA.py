from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

# Carga el modelo entrenado al iniciar
modelo = joblib.load("modelo_ia.pkl")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    bpm = data.get("heart_rate", 0)
    # El modelo predice el estado
    prediction = modelo.predict(np.array([[bpm]]))[0]
    print(f"[IA] BPM recibido: {bpm} -> Estado: {prediction}")
    return jsonify({"condition": prediction})

if __name__ == "__main__":
    app.run(debug=True, port=5000)