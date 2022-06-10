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

    #S: 220 hamburger.edu
    connection_socket.send(bytes(f"220 {host}", "utf-8"))

    standar_message = "mission acumplished by server:\nMisson"

    client_message_1 = connection_socket.recv(1024).decode()

    name = client_message_1.split(" ")[1]
    #S: 250 Hello crepes.fr, pleased to meet you
    connection_socket.send(bytes("250 Hello {}, pleased to meet you".format(name[:-2]), "utf-8"))

    client_message_2 = connection_socket.recv(1024).decode()
    #S: 250 alice@crepes.fr ... Sender ok
    email_rementent = client_message_2[:-2].split("<")
    connection_socket.send(bytes("250 {} ... Sender ok".format(email_rementent[1][:-1]), "utf-8"))

    client_message_3 = connection_socket.recv(1024).decode()
    #S: 250 bob@hamburger.edu ... Recipient ok
    mail_receptor = client_message_3[:-2].split("<")
    connection_socket.send(bytes("250 {} ... Recipient ok".format(mail_receptor[1][:-1]), "utf-8"))
    
    client_message_4 = connection_socket.recv(1024).decode()
    #S: 354 Enter mail, end with “.” on a line by itself
    connection_socket.send(bytes("354 Enter mail, end with “.” on a line by itself", "utf-8"))

    client_message_5 = connection_socket.recv(1024).decode()
    #S: 250 Message accepted for delivery
    connection_socket.send(bytes("250 Message accepted for delivery", "utf-8"))

    client_message_5 = connection_socket.recv(1024).decode()
    #S: 221 hamburger.edu closing connection
    connection_socket.send(bytes(f"221 {host} closing connection", "utf-8"))

    connection_socket.close()

"""
S: 220 hamburger.edu
S: 250 Hello crepes.fr, pleased to meet you
S: 250 alice@crepes.fr ... Sender ok
S: 250 bob@hamburger.edu ... Recipient ok
S: 354 Enter mail, end with “.” on a line by itself
S: 250 Message accepted for delivery
S: 221 hamburger.edu closing connection
"""