from flask import Flask, request, jsonify
import subprocess
import threading
import time

app = Flask(__name__)

@app.route("/waveform", methods=["POST"])
def waveform():
    data = request.get_json()
    print(f"[SIMULADOR] Señal ECG: {data['ecg']}")
    # Aquí puedes almacenar el último dato, o reenviar si es necesario
    return jsonify({"status": "ok"})
@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    bpm = data.get("heart_rate", 0)
    estado = "Normal"
    if bpm < 60:
        estado = "Bajo"
    elif 60 <= bpm <= 100:
        estado = "Normal"
    elif 100 < bpm <= 120:
        estado = "Alerta"
    else:
        estado = "Crítico"
    print(f"[IA] BPM recibido: {bpm} -> Estado: {estado}")
    return jsonify({"condition": estado})

def iniciar_simulador():
    # Espera para asegurar que Flask esté listo
    time.sleep(2)
    subprocess.run(["python", "SimuECG.py"])

if __name__ == "__main__":
    hilo_simulador = threading.Thread(target=iniciar_simulador)
    hilo_simulador.start()
    app.run(debug=True, port=5000)