def create_server():
    pass


presentation = "0: Create a server thread\n" \
               "1: Exit for the program\n"
option = {0: create_server,
          1: exit}

error = "Please enter number in range [0, 1]"


def run():
    while True:
        try:
            read = int(input(presentation +
                             'Your answer: '))
        except:
            print(error)
            continue

        try:
            print(read)
            option[read]()
        except:
            print(error)
            return
