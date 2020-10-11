from socket import *


def smtp_client(port=1025, mailserver='127.0.0.1'):
    msg = "\r\n Ayushi's Assignment"
    endmsg = "\r\n.\r\n"

    # Choose a mail server (e.g. Google mail server) if you want to verify the script beyond GradeScope

    # Create socket called clientSocket and establish a TCP connection with mailserver and port

    # Fill in start
    # Fill in end
    I print ("creando el sooooocket")
    clientSocket = socket(AF_INET,SOCK_STREAM)
    print ("conectando el sooooocket")
    wrappedSocket = ssl.wrap_socket(clientSocket,      #Here we try to create a secure socket to that
                ssl_version=ssl.PROTOCOL_TLSv1,     #the mail server makes a handshake and create the response
                ciphers="HIGH:-aNULL:-eNULL:-PSK:RC4-SHA:RC4-MD5",
                cert_reqs=ssl.CERT_REQUIRED)
    wrappedSocket.connect((mailServer, mailPort))
    


    recv = clientSocket.recv(1024).decode()
    print(recv)
    if recv[:3] != '220':
        print('220 reply not received from server.')

    # Send HELO command and print server response.
    heloCommand = 'HELO Alice\r\n'
    clientSocket.send(heloCommand.encode())
    recv1 = clientSocket.recv(1024).decode()
    print(recv1)
    if recv1[:3] != '250':
        print('250 reply not received from server.')

    Username=raw_input("Insert Username: ")
    Password= getpass.getpass(prompt='Insert Password: ')
    UP=("\000"+Username+"\000"+Password).encode("base64")   
    print UP
    UP=UP.strip("\n")
    login = 'AUTH PLAIN '+ UP + '\r\n'
    print login
    wrappedSocket.send(login)
    recv_from_TLS = wrappedSocket.recv(1024)
    print recv_from_TLS


    # Send MAIL FROM command and print server response.
    # Fill in start
    fromCommand = 'MAIL FROM: <'+ Username+'>\r\n'
    print fromCommand
    wrappedSocket.send(fromCommand)
    recv2 = wrappedSocket.recv(1024)
    print "Este es el recv2: %s" % recv2
    if recv2[:3] != '250':
        print('rcpt2 to 250 reply not received from server, cabron.')
    # Fill in end

    # Send RCPT TO command and print server response.
    receiver =raw_input("Send email to: ")
    # Fill in start
    toCommand = 'RCPT TO: <'+ receiver +'>\r\n'
    print toCommand
    wrappedSocket.send(toCommand)
    recv3 = wrappedSocket.recv(1024)
    print "Este es el recv3: %s" % recv3
    if recv3[:3] != '250':
        print('rcpt3 to 250 reply not received from server, cabron.')

    # Send DATA command and print server response.
    # Fill in start
    dataCommand = 'DATA\r\n'
    print dataCommand
    wrappedSocket.send(dataCommand)
    recv4 = wrappedSocket.recv(1024)
    print recv4
    Subject=raw_input("Subject: ")
    Text=raw_input("Message: ")
    wrappedSocket.send("Subject: "+Subject+"\r\n\r\n"+Text+"\r\n"+ endmsg +"\r\n")
    recv5 = wrappedSocket.recv(1024)
    print recv5
    # Fill in end

    # Send message data.
    # Fill in start
    # Fill in end

    # Message ends with a single period.
    # Fill in start
    # Fill in end

    # Send QUIT command and get server response.
    # Fill in start
    wrappedSocket.send("QUIT\r\n")
    recv6 = wrappedSocket.recv(1024)
    print recv6
    wrappedSocket.close()
    # Fill in end



if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')
