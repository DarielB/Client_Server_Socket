import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost", 12346))

valor = input("Digite o valor em reais (ex: 10): ")
moeda = input("Digite a moeda desejada (dolar, euro, iene): ")

mensagem = f"{valor};{moeda}"
client.send(mensagem.encode())

resposta = client.recv(1024).decode()
print("Resposta do servidor:", resposta)
client.close()
