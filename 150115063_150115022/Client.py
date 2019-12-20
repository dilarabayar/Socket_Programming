import socket
import main

host = socket.gethostname()
port = 5432
BUFFER_SIZE = 2000
tcpClient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpClient.connect(("localhost", port))
string = main.main()
byt=string.encode()
tcpClient.send(byt)
data = tcpClient.recv(1024)
print('Received', repr(data))
tcpClient.close()
