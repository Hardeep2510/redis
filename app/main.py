# Uncomment this to pass the first stage
import socket


def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    print("Logs from your program will appear here!")

    # Uncomment this to pass the first stage

    server_socket = socket.create_server(("localhost", 6379), reuse_port=True)
    server_socket.accept() # wait for client
    redis_socket, return_address = server_socket.accept()  # wait for client
    print(return_address)
    redis_socket.sendall(b"+PONG\r\n")

if __name__ == "__main__":
    main()
