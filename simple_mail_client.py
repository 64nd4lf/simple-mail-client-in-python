from socket import *

sender = 'From:<raghu.p@aol.com>\r\n'
to = 'To:<pusaparv@mail.uc.edu>\r\n'
subject = 'Subject:Learning to mail\r\n'
msg = "\r\n I love computer networks!"
endmsg = "\r\n.\r\n"

# Choose a mail server
mailserver = 'smtp.aol.com' 
serverPort = 587
# Create socket called clientSocket and establish a TCP connection with mailserver

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((mailserver, serverPort))

recv = clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != '220':
	print('220 reply not received from server.')

# Send HELO command and print server response.

heloCommand = 'EHLO Alice\r\n'
clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)
if recv1[:3] != '250':
    print('250 reply not received from server.')

# Perform authentication
clientSocket.send('AUTH LOGIN\r\n')
recv1 = clientSocket.recv(1024)
print recv1
if recv1[:3] != '334':
	print '334 reply not received from server'
else:
	clientSocket.send('cmFnaHUucEBhb2wuY29t\r\n') #base64 encoding of mail ID
	recv1 = clientSocket.recv(1024)
	print recv1
	if recv1[:3] != '334':
		print '334 reply not received'
	else:
		clientSocket.send('cHJvamVjdDFAQ04=\r\n') #base64 encoding of the email password.
		recv1 = clientSocket.recv(1024)
		print recv1
		if recv1[:3] != '235':
			print '235 reply not received from server'

# Send MAIL FROM command and print server response.

mailFrom = 'MAIL FROM:<raghu.p@aol.com>\r\n'
clientSocket.send(mailFrom)

recv1 = clientSocket.recv(1024)
print recv1


# Send RCPT TO command and print server response. 

rcptTo = 'RCPT TO:<pusaparv@mail.uc.edu>\r\n'
clientSocket.send(rcptTo)

recv1 = clientSocket.recv(1024)
print recv1


# Send DATA command and print server response. 

clientSocket.send('DATA\r\n')
recv1 = clientSocket.recv(1024)
print recv1


# Send message data.

clientSocket.send(sender)
clientSocket.send(to)
clientSocket.send(subject)
clientSocket.send(msg)


# Message ends with a single period.

clientSocket.send(endmsg)


# Send QUIT command and get server response.

clientSocket.send('QUIT')
recv1 = clientSocket.recv(1024)
print recv1
