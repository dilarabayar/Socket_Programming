#muthi thraeded server: tcp server socket programme stub
import socket
import check_available_room
from threading import Thread

from pip._vendor.distlib.compat import  raw_input


class ClientThread(Thread):
    def  __init__(self,ip,port):
        Thread.__init__(self)
        self.ip=ip
        self.port=port
        print ("[+] New server socket thread started for "+ ip +":"+str(port))

        def run(self):
            while True:
                data=conn.recv(2048)
                print ("Server received data:", data)
                MESSAGE= raw_input("Multi threaded server: Enter response from server/enter exit:")
                if MESSAGE == 'exit':
                    break
                conn.send(MESSAGE) #echo

TCP_IP='localhost'
TCP_PORT= 5432
BUFFER_SIZE=2000 # usually 1024 but we need quick response
tcpServer=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
tcpServer.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
tcpServer.bind((TCP_IP,TCP_PORT))
threads=[]
def define_port(host):

    if (host == "www.hotel.com"):
        print("define PORT 7777\n")
        return 7777
    elif (host == "www.airline.com"):
        print("define PORT 5433\n")
        return 5433
    else:
        print("404")
        return 0

##this section for http request
def httpRequest(target_address,host):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    target_port =define_port(host)
    print("target port > ",target_port,"\n")
    client.connect(("localhost", target_port))
    target = target_address.split("-")
    # send some data
    request = ("GET / HTTP/1.1\r\nHost:%s\r\n%s/%s/%s/%s/%s\r\n\r\n" % (host,target[0],target[1],target[2],target[3],target[4]))
    client.send(request.encode())
    # receive some data
    response = client.recv(4096)
    http_response = repr(response)
    client.close()

while True:
    tcpServer.listen(4)
    print("multithreaded python server : waiting for conncetions from tcp clients...")
    (conn,(ip,port))=tcpServer.accept()
    newthread=ClientThread(ip, port)
    newthread.start()
    threads.append(newthread)
    while True:
        try:
            data = conn.recv(1024)
            if not data: break
            string = data.decode()
            print(" Main Client Says: " + string)
            httpRequest(string,"www.hotel.com")
             #httpRequest(string,"www.airline.com")
            conn.sendall(b'Hotel Server Says:hi')

        except socket.error:
            print("Error Occured.")
            break

for t in thraeds:
    t.join()

