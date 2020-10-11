from socket import *


def smtp_client(port=1025, mailserver='127.0.0.1'):
    msg = "\r\n My message"
    endmsg = "\r\n.\r\n"

    # Choose a mail server (e.g. Google mail server) if you want to verify the script beyond GradeScope

    # Create socket called clientSocket and establish a TCP connection with mailserver and port

    # Fill in start
    clientSocket = socket(AF_INET,SOCK_STREAM)
    clientSocket.connect((mailserver,port))
    # Fill in end

    recv = clientSocket.recv(1024).decode()

    # Send HELO command and print server response.
    heloCommand = 'HELO Alice\r\n'
    clientSocket.send(heloCommand.encode())
    recv1 = clientSocket.recv(1024).decode()

    # Send MAIL FROM command and print server response.
    # Fill in start
    clientSocket.send('MAIL FROM: <gupta.ashi111@gmail.com>\r\n'.encode())
    mail_command_recv = clientSocket.recv(1024).decode()
    # Fill in end

    # Send RCPT TO command and print server response.
    # Fill in start
    clientSocket.send('RCPT TO: <gupta.ashi111@gmail.com>\r\n'.encode())
    rcpt_comment_recv = clientSocket.recv(1024).decode()
    # Fill in end

    # Send DATA command and print server response.
    # Fill in start
    clientSocket.send('Data\r\n'.encode())
    data_command_recv = clientSocket.recv(1024).decode()
    # Fill in end

    # Send message data.
    # Fill in start
    clientSocket.send(msg.encode())
    # Fill in end

    # Message ends with a single period.
    # Fill in start
    clientSocket.send(endmsg.encode())
    msg_recv = clientSocket.recv(1024).decode()
    # Fill in end

    # Send QUIT command and get server response.
    # Fill in start
    quit_command = 'Quit\r\n'
    clientSocket.send(quit_command.encode())
    quit_command_recv = clientSocket.recv(1024).decode()
    clientSocket.close()
    # Fill in end


if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')
