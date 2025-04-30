import socket
import threading

HOST = '127.0.0.1'  # Replace with your server's IP address
PORT = 12345

def handle_client(client_socket, client_address):
    print(f"[*] Accepted connection from {client_address[0]}:{client_address[1]}")
    try:
        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            print(f"[*] Received: {data.decode('utf-8')} from {client_address[0]}:{client_address[1]}")

            # In a real VPN, you would forward this data to the intended destination
            # and send the response back to the client.
            response = f"Server received: {data.decode('utf-8')}".encode('utf-8')
            client_socket.sendall(response)

    except Exception as e:
        print(f"[*] Error handling client {client_address}: {e}")
    finally:
        print(f"[*] Connection closed with {client_address[0]}:{client_address[1]}")
        client_socket.close()

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        server.bind((HOST, PORT))
        server.listen()
        print(f"[*] Listening on {HOST}:{PORT}")
        while True:
            client_socket, client_address = server.accept()
            client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
            client_thread.start()
    except Exception as e:
        print(f"[*] Error starting server: {e}")
    finally:
        server.close()

if __name__ == "__main__":
    start_server()