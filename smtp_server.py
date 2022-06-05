from socket import *

host = "localhost"
port = 3000

server_socker = socket(AF_INET, SOCK_STREAM)
server_socker.bind((host, port))
server_socker.listen(9)

print("Server is ronning at socket port: {}".format(port))

while True:
    connection_socket, andress = server_socker.accept()
    print("conected to client data: {}".format(andress))
    connection_socket.send(bytes("200", "utf-8"))

    standar_message = "mission acumplished by server:\nMisson"

    client_message_1 = connection_socket.recv(1024).decode()
    connection_socket.send(bytes("{}: {}".format(standar_message, client_message_1), "utf-8"))

    client_message_2 = connection_socket.recv(1024).decode()
    connection_socket.send(bytes("{}: {}".format(standar_message, client_message_2), "utf-8"))

    client_message_3 = connection_socket.recv(1024).decode()
    connection_socket.send(bytes("{}: {}".format(standar_message, client_message_3), "utf-8"))
    
    client_message_4 = connection_socket.recv(1024).decode()
    connection_socket.send(bytes("{}: {}".format(standar_message, client_message_4), "utf-8"))

    client_message_5 = connection_socket.recv(1024).decode()
    connection_socket.send(bytes("{}: {}".format(standar_message, client_message_5), "utf-8"))

    client_message_5 = connection_socket.recv(1024).decode()
    connection_socket.send(bytes("{}: {}".format(standar_message, client_message_5), "utf-8"))

    client_message_5 = connection_socket.recv(1024).decode()
    connection_socket.send(bytes("{}: {}".format(standar_message, client_message_5), "utf-8"))

    client_message_7 = connection_socket.recv(1024).decode()
    connection_socket.send(bytes("{}: {}".format(standar_message, client_message_7), "utf-8"))

    connection_socket.close()