import socket

# Criação do cliente usando o protocolo TCP e conexão com o servidor localizado na porta 12346
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost", 12346))

# Entrada dos dados pelo usuário
valor = input("Digite o valor em reais (ex: 10): ")
moeda = input("Digite a moeda desejada (dolar, euro, iene): ")

# Adequação dos dados de entrada do programa para serem enviados para o servidor
mensagem = f"{valor};{moeda}"

# Envio da mensagem codificada para o servidor
client.send(mensagem.encode())

# Obtenção da resposta do servidor
resposta = client.recv(1024).decode()

# Exibição da resposta do servidor
print("Resposta do servidor:", resposta)

# Fechamento da conexão do cliente com o servidor
client.close()
