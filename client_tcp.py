import socket


# Define socket host and port
SERVER_HOST = '0.0.0.0'
SERVER_PORT = 80

# Create socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((SERVER_HOST, SERVER_PORT))
server_socket.listen(1)
print('Listening to host: %s' % SERVER_HOST + ' port: %s' % SERVER_PORT)

while True:
    client_connection, client_address = server_socket.accept()
    request = client_connection.recv(1024).decode()
    print(request)
    headers = request.split('\n')
    filename = headers[0].split()[1]
    if filename == '/':
        filename = '/index.html'
    if filename == '/kotik':
        filename = '/kotik.html'
    try:
        data = open('data' + filename, mode='rb')
        content = data.read()
        data.close()
        response = 'HTTP/1.1 200 OK\n\n'.encode() + content
    except FileNotFoundError:
        response = 'HTTP/1.1 404 NOT FOUND\n\nFile Not Found.encode()'.encode()

    client_connection.sendall(response)
    client_connection.close()
server_socket.close()