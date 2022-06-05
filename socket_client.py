from socket import *

server_name = "localhost"
server_port  = 3000
client_socket = socket( AF_INET, SOCK_STREAM)
client_socket.connect((server_name, server_port))
sentence = input("input lower case sentence: ")
client_socket.send(bytes(sentence, "utf-8"))
modified_sentence = client_socket.recv(1024)
print("From server side: {}".format(modified_sentence.decode("utf-8")))
client_socket.close()