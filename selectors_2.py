import socket
import selectors

selector = selectors.DefaultSelector()
i = 0
def server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    server_socket.bind(('127.0.0.1',8000))
    server_socket.listen()
    selector.register(fileobj=server_socket, events=selectors.EVENT_READ, data=accept_connection)


def accept_connection(server_socket):
    print("Accept connection")
    client_socket, addr = server_socket.accept()
    selector.register(fileobj=client_socket, events=selectors.EVENT_READ, data=send_message)


def send_message(client_socket):
    global  i
    print("Wait request")
    request = client_socket.recv(4096)

    if  request:
        print("Send")
        i += 1
        response = ("HTTP/1.1 200 OK\n\n<h1>Hello world</h1><h2>"+i.__str__()+"/<h2").encode()
        client_socket.send(response)
    else:
        print("Close")
        selector.unregister(client_socket)
        client_socket.close()


def event_loop():
    while True:
        events = selector.select()
        for key, _ in events:
            callback = key.data
            callback(key.fileobj)

if __name__ == "__main__":
    server()
    event_loop()



