import socket

def ping():
    # to ping a particular PORT at an IP
    # if the machine won't receive any packets from
    # the server for more than 3 seconds
    # i.e no connection is
    # made(machine doesn't have a live internet connection)
    # <except> part will be executed
    try:
        socket.setdefaulttimeout(3)

        # AF_INET: address family (IPv4)
        # SOCK_STREAM: type for TCP (PORT)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        host = "8.8.8.8"
        port = 53

        server_address = (host, port)

        # send connection request to the defined server
        s.connect(server_address)

    except OSError as error:

        # function returning false after
        # data interruption(no connection)
        return False
    else:

        # the connection is closed after
        # machine being connected
        s.close()
        return True

# print(ping())