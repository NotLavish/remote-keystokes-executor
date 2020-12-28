import socket
import select
import threading

class Server:
    def __init__(self):
        self.start()
        
    def start(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        self.ip = socket.gethostname()
        self.port = 2222
        
        self.clients = []
        
        self.username = {}
        
        self.s.bind((self.ip, self.port))
        self.s.listen(5)
        
        print(f"Opening server on {socket.gethostbyname(socket.gethostname())}")
        while True:
            client, address = self.s.accept()
            
            username = client.recv(1024).decode()
            
            self.username[client] = username
            self.clients.append(client)
            
            print(f"{self.username[client]} has joined")
            thread = threading.Thread(target=self.handler, args=(client, address,))
            thread.start()
     
    def send(self, msg, client):
        try:
            if self.username[client] == 'sender':
                value = list(self.username.keys())[list(self.username.values()).index("recv")]
                reciever = value
                reciever.send(msg.encode())
        except:
            pass
            
    def handler(self, client, address):
        while True:
            try:
                msg = client.recv(5024).decode()
                self.send(msg, client)
            except:
                self.clients.remove(client)
                self.username.pop(client)
                break
server = Server()