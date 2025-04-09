import socket

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

valor = input("Digite o valor em reais (ex: 10): ")
moeda = input("Digite a moeda desejada (dolar, euro, iene): ")

mensagem = f"{valor};{moeda}"
client.sendto(mensagem.encode(), ("localhost", 12345))

resposta, _ = client.recvfrom(1024)
print("Resposta do servidor:", resposta.decode())
client.close()
