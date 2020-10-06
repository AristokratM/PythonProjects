import  socket
from  select import select
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
server_socket.bind(('127.0.0.1',8000))
server_socket.listen()
to_monitor = []
def accept_connection(server_socket):
    print("Accept connection")
    client_socket, addr = server_socket.accept()
    to_monitor.append(client_socket)

def send_message(client_socket):
    print("Wait request")
    request = client_socket.recv(4096)

    if  request:
        print("Send")
        response = "HTTP/1.1 200 OK\n\n<h1>Hello world</h1>".encode()
        client_socket.send(response)
    else:
        print("Close")
        to_monitor.remove(client_socket)
        client_socket.close()


def event_loop():
    while True:
        print("Wait to Ready")
        ready_to_read,_,_ = select(to_monitor,[],[])
        for soc in ready_to_read:
            if soc is server_socket:
                accept_connection(soc)
            else:
                send_message(soc)
if __name__ == "__main__":
    to_monitor.append(server_socket)
    event_loop()



