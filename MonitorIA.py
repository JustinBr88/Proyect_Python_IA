import asyncio
import websockets
import joblib
import numpy as np
import json

# Carga el modelo entrenado al iniciar
modelo = joblib.load("modelo_ia.pkl")

async def handler(websocket):
    print("[IA] Cliente conectado. Esperando datos BPM...")
    try:
        async for message in websocket:
            try:
                data = json.loads(message)
                bpm = data.get("heart_rate", 0)
                prediction = modelo.predict(np.array([[bpm]]))[0]
                respuesta = f"[IA] BPM recibido: {bpm} -> Estado: {prediction}"
                print(respuesta)
                # Responde al cliente ( modificar aquí para enviar a la app)
                await websocket.send(json.dumps({"condition": str(prediction)}))
            except Exception as e:
                print(f"[IA] Error procesando mensaje: {e}")
                await websocket.send(json.dumps({"error": "Formato de mensaje incorrecto"}))
    except websockets.exceptions.ConnectionClosed as e:
        print("[IA] Conexión WebSocket cerrada.")

async def main():
    print("[IA] Buscando conexión (servidor WebSocket iniciando en 0.0.0.0:8765)...")
    async with websockets.serve(handler, "0.0.0.0", 8765):
        print("[IA] Servidor WebSocket listo y esperando conexiones.")
        await asyncio.Future()  # run forever

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n[IA] Servidor detenido manualmente.")