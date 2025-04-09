import socket

# Criação do cliente usando o protocolo UDP
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Entrada dos dados pelo usuário
valor = input("Digite o valor em reais (ex: 10): ")
moeda = input("Digite a moeda desejada (dolar, euro, iene): ")

mensagem = f"{valor};{moeda}"

# Envio da mensagem codificada para o servidor localizado na porta 12345
client.sendto(mensagem.encode(), ("localhost", 12345))

# Obtenção da resposta do servidor
resposta, _ = client.recvfrom(1024)

# Exibição da resposta do servidor
print("Resposta do servidor:", resposta.decode())

# Fechamento da conexão do cliente com o servidor
client.close()
