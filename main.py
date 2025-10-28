import socket
import threading

HOST, PORT = '', 8888

def handle_client(client_connection):
    request_data = client_connection.recv(1024)
    print(request_data.decode('utf-8'))

    http_response = b"HTTP/1.1 200 OK\r\nContent-Length: 13\r\n\r\nHello, World!"
    client_connection.sendall(http_response)
    client_connection.close()

listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listen_socket.bind((HOST, PORT))
listen_socket.listen(5)
print(f'Serving HTTP on port {PORT} ...')

while True:
    client_connection, client_address = listen_socket.accept()
    threading.Thread(target=handle_client, args=(client_connection,)).start()
