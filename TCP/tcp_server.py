import socket
import random

def converter(valor, moeda):
    taxas = {
        "dolar": round(random.uniform(4.5, 5.5), 2),
        "euro": round(random.uniform(5.0, 6.0), 2),
        "iene": round(random.uniform(0.03, 0.05), 4)
    }
    taxa = taxas.get(moeda.lower(), None)
    if taxa:
        return f"{valor} BRL = {valor / taxa:.2f} {moeda.upper()} (Taxa: {taxa})"
    return "Moeda não suportada."

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 12346))
server.listen(1)
print("Servidor TCP aguardando conexões...")

while True:
    conn, addr = server.accept()
    print(f"Conexão de {addr}")
    data = conn.recv(1024).decode()
    try:
        valor, moeda = data.split(";")
        resultado = converter(float(valor), moeda)
    except:
        resultado = "Erro no formato. Use: <valor>;<moeda>"
    conn.send(resultado.encode())
    conn.close()
