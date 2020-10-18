from socket import *


def smtp_client(port=1025, mailserver='127.0.0.1'):
    msg = "\r\n My message"
    endmsg = "\r\n.\r\n"
    username="gupta,ashi111@gmail.com"
    # Choose a mail server (e.g. Google mail server) if you want to verify the script beyond GradeScope

    # Create socket called clientSocket and establish a TCP connection with mailserver and port

    # Fill in start
    clientSocket = socket(AF_INET,SOCK_STREAM)
    clientSocket.connect((mailserver,port))
    # Fill in end

    recv = clientSocket.recv(1024).decode()
    #print(recv)
    #if recv[:3] != '220':
    #    print('220 reply not received from server.')

    # Send HELO command and print server response.
    #heloCommand = 'HELO Alice\r\n'
    #clientSocket.send(heloCommand.encode())
    #recv1 = clientSocket.recv(1024).decode()
    heloCommand = 'HELO Alice\r\n'
    #print heloCommand
    clientSocket.send(heloCommand)
    recv1 = wrappedSocket.recv(1024)

    # Send MAIL FROM command and print server response.
    # Fill in start
    mail_command = 'MAIL FROM: <'+username+'>\r\n'
    clientSocket.send(mail_command.encode())
    mail_command_recv = clientSocket.recv(1024).decode()
    # Fill in end

    # Send RCPT TO command and print server response.
    # Fill in start
    #rcptToCommand = 'RCPT TO: <gupta.ashi111@gmail.com>\r\n'
    rcpt_to= 'RCPT TO: <'+username+'>\r\n'
    clientSocket.send(rcpt_to.encode())
    rcpt_comment_recv = clientSocket.recv(1024).decode()
    #print(recv3)
    #if recv3[:3] != '250':
    #    print('250 reply not received from server.')
    # Fill in end
    # Send DATA command and print server response.
    # Fill in start
    #dataCommand = 'DATA\r\n'
    clientSocket.send('Data\r\n'.encode())
    data_command_recv = clientSocket.recv(1024).decode()
    #print(recv4)
    #if recv4[:3] != '250':
    #    print('250 reply not received from server.')
    # Fill in end

    # Send message data.
    # Fill in start
    clientSocket.send(msg.encode())
    # Fill in end

    # Message ends with a single period.
    # Fill in start
    clientSocket.send(endmsg.encode())
    msg_recv = clientSocket.recv(1024).decode()
    #print(recv5)
    # Fill in end

    # Send QUIT command and get server response.
    # Fill in start
    quit_command = 'Quit\r\n'
    clientSocket.send(quit_command.encode())
    quit_command_recv = clientSocket.recv(1024).decode()
    #print(recv6)
    clientSocket.close()
    # Fill in end


if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')
