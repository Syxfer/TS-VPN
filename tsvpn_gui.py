import tkinter as tk
from tkinter import ttk
import socket
import threading

class TSVPNClient:
    def __init__(self, root):
        self.root = root
        self.root.title("TS VPN")

        self.server_ip_label = ttk.Label(root, text="Server IP:")
        self.server_ip_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.server_ip_entry = ttk.Entry(root)
        self.server_ip_entry.insert(0, "127.0.0.1")  # Default localhost
        self.server_ip_entry.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

        self.port_label = ttk.Label(root, text="Port:")
        self.port_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.port_entry = ttk.Entry(root)
        self.port_entry.insert(0, "12345")  # Default port
        self.port_entry.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

        self.connect_button = ttk.Button(root, text="Connect", command=self.connect_to_server)
        self.connect_button.grid(row=2, column=0, columnspan=2, padx=5, pady=10)

        self.message_label = ttk.Label(root, text="Message:")
        self.message_label.grid(row=3, column=0, padx=5, pady=5, sticky="w")
        self.message_entry = ttk.Entry(root)
        self.message_entry.grid(row=3, column=1, padx=5, pady=5, sticky="ew")

        self.send_button = ttk.Button(root, text="Send", command=self.send_message, state=tk.DISABLED)
        self.send_button.grid(row=4, column=0, columnspan=2, padx=5, pady=10)

        self.response_label = ttk.Label(root, text="Server Response:")
        self.response_label.grid(row=5, column=0, padx=5, pady=5, sticky="w")
        self.response_text = tk.StringVar()
        self.response_display = ttk.Label(root, textvariable=self.response_text)
        self.response_display.grid(row=5, column=1, padx=5, pady=5, sticky="ew")

        self.client_socket = None
        self.receive_thread = None

    def connect_to_server(self):
        server_ip = self.server_ip_entry.get()
        port = int(self.port_entry.get())

        try:
            self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.client_socket.connect((server_ip, port))
            self.connect_button.config(state=tk.DISABLED, text="Connected")
            self.send_button.config(state=tk.NORMAL)
            self.start_receiving()
            print(f"[*] Connected to {server_ip}:{port}")
        except Exception as e:
            self.response_text.set(f"Error connecting: {e}")
            print(f"[*] Error connecting to server: {e}")
            self.client_socket = None

    def start_receiving(self):
        self.receive_thread = threading.Thread(target=self.receive_data)
        self.receive_thread.daemon = True
        self.receive_thread.start()

    def receive_data(self):
        try:
            while True:
                data = self.client_socket.recv(1024)
                if not data:
                    break
                self.response_text.set(f"{data.decode('utf-8')}")
        except Exception as e:
            print(f"[*] Error receiving data: {e}")
        finally:
            if self.client_socket:
                self.client_socket.close()
                self.client_socket = None
                self.connect_button.config(state=tk.NORMAL, text="Connect")
                self.send_button.config(state=tk.DISABLED)

    def send_message(self):
        if self.client_socket:
            message = self.message_entry.get()
            try:
                self.client_socket.sendall(message.encode('utf-8'))
                self.message_entry.delete(0, tk.END)
            except Exception as e:
                self.response_text.set(f"Error sending message: {e}")
                print(f"[*] Error sending message: {e}")
        else:
            self.response_text.set("Not connected to the server.")

if __name__ == "__main__":
    root = tk.Tk()
    app = TSVPNClient(root)
    root.mainloop()