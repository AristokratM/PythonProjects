import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(('127.0.0.1', 8000))
server_socket.listen()

while True:
    client_socket, addr = server_socket.accept()
    while True:
        request = client_socket.recv(4096)
        if not request:
            break
        else:
            response = "HTTP/1.1 200 OK\n\n<h1>Hello World!</h1>".encode()
            client_socket.send(response)
    client_socket.close()