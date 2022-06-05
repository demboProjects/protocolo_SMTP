from socket import *
endmsg = "\r\n.\r\n"

sender_email = input("Enter your user email: ")
dest_email = input("Enter destination user email: ")
msg = input("Enter your message: ")
# Choose a mail server (e.g. Google mail server) and call it mailserver
 #Fill in start
mailserver = "localhost"
serverPort = 3000
 #  #Fill in end

# Create socket called clientSocket and establish a TCP connection with mailserver
#Fill in start 
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((mailserver, serverPort))
#Fill in end

recv = clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != '220':
    ...
print('220 reply not received from server.')

# Send HELO command and print server response.
heloCommand = 'HELO Alice\r\n'
clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)
if recv1[:3] != '250':
 print('250 reply not received from server.')
 
# Send MAIL FROM command and print server response.
# Fill in start
mail_data = "MAIL FROM: <josedembo18@aluno.edu.br>\r\n"
clientSocket.send(mail_data.encode())

recv2 = clientSocket.recv(1024).decode()
print(recv2)
# Fill in end

# Send RCPT TO command and print server response. 
# Fill in start
rcpt_data = "RCPT TO: <josepedrodanieldembo@gmail.com>\r\n".encode()
clientSocket.send(rcpt_data)

recv3 = clientSocket.recv(1024).decode()
print(recv3)
# Fill in end
# Send DATA command and print server response. 
# Fill in start
data_command = "DATA\r\n".encode()
clientSocket.send(data_command)

recv4 = clientSocket.recv(1024).decode()
print(recv4)
# Fill in end

# Send message data.
# Fill in start
message = "subjetc: {}\r\n".format(msg).encode()
clientSocket.send(message)

recv5 = clientSocket.recv(1024).decode()
print(recv5)
# Fill in end

# Message ends with a single period.
# Fill in start
end_message = "{}".format(endmsg).encode()
clientSocket.send(end_message)

recv6 = clientSocket.recv(1024).decode()
print(recv6)
# Fill in end

# Send QUIT command and get server response.
# Fill in start
quit_commmand = "QUIT\r\n".encode()
clientSocket.send(quit_commmand)

recv7 = clientSocket.recv(1024).decode()
print(recv7)

clientSocket.close()
# Fill in end