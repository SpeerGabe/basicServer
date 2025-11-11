import socket
import time
# I watched the following video to learn how to set up a http python server with the python socket module
# https://www.youtube.com/watch?v=Hncp0mPfUvk&t=167s

# Define server address and port
SERVER_HOST = "127.0.0.1"
SERVER_PORT = 8040
# Creates a TCP socket with IPv4
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#changes default behavior of socket and enables you to reuse the local address and port instead of wating on time out
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#specifies 127.0.0.1 as the IP address and 8040 as the port number
server_socket.bind((SERVER_HOST, SERVER_PORT))

#enables the server to accept connections, with a maximum of 5 connections
server_socket.listen(5)

print("Listening on port {SERVER_PORT}")

#allows for sending and receiving data from clients
while True:
    try:
        client_socket, client_address = server_socket.accept()
        #shows client socket and address
        request = client_socket.recv(1500).decode()
        print(request)
        #prints out the http version and path
        headers = request.split("\n")
        first_header_components = headers[0].split()
        
        htpp_version = first_header_components[0]
        path = first_header_components[1]
        
        if path == "/":
            fin = open("index.html")
            content = fin.read()
            fin.close()
            
            #STATUS LINE -
            #HEADERS
            #MESSAGE-BODY
            response = "hTTP/1.1 200 OK\n\n" + content
            client_socket.sendall(response.encode())
            client_socket.close()
#error handling
    except:
#delay by one second
        time.sleep(1)
        print("Error Caught!")
        continue