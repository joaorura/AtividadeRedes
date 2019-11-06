import socket
from threading import Thread


class Lister(Thread):
    def __init__(self, server_input, address):
        Thread.__init__(self)

        self.server_input = server_input
        self.address = address

    def run(self):
        print("New connection of " + self.address)

        while True:
            response = self.server_input.recv(1024)
            response = response.rstrip()
            if response != "sair":
                print("Message of client:", response)
            else:
                break


class Socket:
    def __init__(self, ip_address, port):
        if type(ip_address) != str or type(port) != int:
            raise ValueError()

        self.address = (ip_address, port)
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind(self.address)

    def start_listen(self):
        print("\n\nStart Listening")
        
        while True:
            self.server_socket.listen(1)
            aux = self.server_socket.accept()
            lister = Lister(aux)
            lister.run()
