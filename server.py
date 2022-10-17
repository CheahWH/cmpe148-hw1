import socket

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)
print('Python server is running..')

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # The .bind() method is used to associate the socket with a specific network interface and port number
    s.bind((HOST, PORT))
    s.listen()  # enables a server to accept connections
    # The .accept() method blocks execution and waits for an incoming connection.
    conn, addr = s.accept()
    # When a client connects, it returns a new socket object representing the connection and a tuple holding the address of the client.
    # The tuple will contain (host, port) for IPv4 connections

    with conn:
        print(f"Connected by client: {addr}")
        conn.send(bytes("YOU JUST WON 500 DOLLARS!!!", "utf-8"))
