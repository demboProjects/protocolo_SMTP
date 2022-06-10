from socket import *
from telnetlib import IP
endmsg = "\r\n.\r\n"
print(gethostbyname("localhost"))
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
    print('220 reply not received from server.')

print("220 response received from server")

# Send HELO command and print server response.
heloCommand = 'HELO Alice\r\n'
clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(1024).decode()
print(f"\n{recv1}")
if recv1[:3] != '250':
    print('250 reply not received from server.')
 
# Send MAIL FROM command and print server response.
# Fill in start
sender_email = input("Enter your user email: ")
mail_data = f"MAIL FROM: <{sender_email}>\r\n"
clientSocket.send(mail_data.encode())

recv2 = clientSocket.recv(1024).decode()
print(recv2,"\n")
# Fill in end

# Send RCPT TO command and print server response. 
# Fill in start

dest_email = input("Enter destination user email: ")
rcpt_data = f"RCPT TO: <{dest_email}>\r\n".encode()
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
msg = input("Enter your message: ")
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