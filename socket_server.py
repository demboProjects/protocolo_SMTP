from socket import *


server_port  = 3000
server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.bind(("localhost", server_port))
server_socket.listen(1)
print("Server is ready to receive")

while 1:
    connection_socket, addr = server_socket.accept()
    sentence = connection_socket.recv(1024)
    captalize_sentence = sentence.decode("utf-8").upper()
    connection_socket.send(bytes(captalize_sentence, "utf-8"))
    connection_socket.close()