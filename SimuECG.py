import socket
import time
import random

HOST = '0.0.0.0'
PORT = 12345

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(1)
print("Esperando conexión del cliente (Android)...")

while True:
    conn, addr = server_socket.accept()
    print(f"Conexión aceptada de {addr}")
    try:
        while True:
            bpm = round(random.uniform(60, 100), 2)
            conn.sendall(f"{bpm}\n".encode())
            print(f"Enviado: {bpm}")
            time.sleep(1)
    except Exception as e:
        print("Error:", e)
    finally:
        conn.close()