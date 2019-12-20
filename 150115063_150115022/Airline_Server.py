# muthi thraeded server: tcp server socket programme stub
import socket
from threading import Thread
import check_available_room

from pip._vendor.distlib.compat import raw_input


class ClientThread(Thread):
    def __init__(self, ip, port):
        Thread.__init__(self)
        self.ip = ip
        self.port = port
        print("[+] New airline server socket thread started for " + ip + ":" + str(port))

        def run(self):
            while True:
                data = conn.recv(2048)
                print("Server received data:", data)
                MESSAGE = raw_input("Multi threaded server: Enter response from server/enter exit:")
                if MESSAGE == 'exit':
                    break
                conn.send(MESSAGE)  # echo


TCP_IP = 'localhost'
TCP_PORT = 5432
BUFFER_SIZE = 2000  # usually 1024 but we need quick response
tcpServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpServer.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
tcpServer.bind((TCP_IP, TCP_PORT))
threads = []


def check_host(host):
    if "www.airline.com" in host:
        return 1
    else:
        return 0


while True:
    tcpServer.listen(4)
    print("multithreaded airline server : waiting for conncetions from http clients...")
    (conn, (ip, port)) = tcpServer.accept()
    newthread = ClientThread(ip, port)
    newthread.start()
    threads.append(newthread)
    while True:
        try:
            data = conn.recv(1024)

            if not data: break
            string = data.decode()
            if check_host(string):
                p = 1
            # check_available_flight(string)
            else:
                break
            print("airline Client Says: " + string)
            conn.sendall(b'airline Server Says:hi')

        except socket.error:
            print("Error Occured.")
            break

for t in thraeds:
    t.join()
