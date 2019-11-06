from server.socket import Socket


def create_socket():
    print("Starting socket")
    ip_address = input("Ip: ")
    port = int(input("Port: "))

    try:
        socket = Socket(ip_address, port)
    except ValueError:
        print("Error in create a socket\n\n")
        run()
        return

    socket.start_listen()


def out():
    print("\n\nLeaving the program")
    pass


presentation = "0: Create a server thread\n" \
               "1: Exit for the program\n"
option = {0: create_socket,
          1: out}

error = "Please enter number in range [0, 1]"


def run():
    try:
        read = int(input(presentation + 'Your answer: '))
    except ValueError:
        print(error)

    try:
        option[read]()
    except KeyError:
        print(error)
