from socket import *
mailserver = 'localhost'#Fill in start #Fill in end
port = 25

# Create socket called clientSocket and establish a TCP connection with mailserver
#Fill in start
clientSocket = socket(AF_INET,SOCK_STREAM)
clientSocket.connect((mailserver,port))
#Fill in end
recv = clientSocket.recv(1024)
print recv

if recv[:3] != '220':
    print '220 reply not received from server.'
# Send HELO command and print server response.
helloCommand = 'HELLO\r\n'
print "Sending first message "
clientSocket.send(helloCommand)
echo = clientSocket.recv(1024)
print echo
if echo[:3] != '250':
    print "250 reply not received from server."

# Send MAIL FROM command and print server response.
print 'Sending MAIL FROM Command'
mailFromCommand = 'MAIL FROM: username@domain.com\r\n'
clientSocket.send(mailFromCommand)
echo = clientSocket.recv(1024)
print echo
if echo[:3] != '250':
    print "250 reply not receved from server"
# Send RCPT TO command and print server response.
print "Sending RCPT TO command"
rcptToCommand = 'RCPT TO: username@domain.com\r\n'
clientSocket.send(rcptToCommand)
echo = clientSocket.recv(1024)
print echo
if echo[:3] !='250':
    print "250 reply not received from server"
# Send DATA command and print server response.
print "Sending DATA command"
dComand = 'Data\r\n'
clientSocket.send(dComand)
echo = clientSocket.recv(1024)
print echo
if echo[:3]!= '354':
    print "354 reply not received from server"

# Send message data.
print "Sending message"
message = 'SUBJECT:SMTP Mail Client Test.\r\n'
clientSocket.send(message)
echo = clientSocket.recv(1024)
print echo
if echo[:3]!= '250':
    print "250 reply not received from server"
# Send QUIT command and get server response.
qcommand = 'QUIT\r\n'
clientSocket.send(qcommand)
echo = clientSocket.recv(1024)
print echo
if echo[:3]!= '221':
    print "221 reply not recieved from server"


