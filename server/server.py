import socket
from threading import Thread


class Lister(Thread):
    def __init__(self, server_input, address):
        Thread.__init__(self)

        self.server_input = server_input
        self.address = address

    def run(self):
        print(f'New connection of {self.address}\n\n')

        while True:
            try:
                response = self.server_input.recv(1024)
            except ConnectionResetError:
                break

            response = response.decode()
            response = response.rstrip()
            if response != "exit":
                print(f"Message of client [{self.address[1]}]:", response)
            else:
                break

        print('End connection')


class Socket:
    def __init__(self, ip_address, port):
        if type(ip_address) != str or type(port) != int:
            raise ValueError()

        self.address = (ip_address, port)
        self.server_socket = socket.socket()
        self.server_socket.bind(self.address)

    def start_listen(self):
        print("\n\nStart Listening")
        self.server_socket.listen(1)

        while True:
            aux = self.server_socket.accept()
            lister = Lister(aux[0], aux[1])
            lister.start()
