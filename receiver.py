import socket
import threading
import keyboard

class Receiver:
    def __init__(self):
        self.connection()
        
    def connection(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        #self.ip = input("IP: ")
        #self.port = input("PORT: ")
        
        #self.ip = socket.gethostname()
        #self.port = 2222
        
        self.s.connect((self.ip, self.port))
        
        self.username = 'recv'
        self.s.send(self.username.encode())
        
        print(f"u da {self.username}")
        
        input_handler = threading.Thread(target=self.input_handler,args=())
        input_handler.start()
        
    def input_handler(self):
        while True:
            msg = self.s.recv(1024).decode()
            keystrokes = msg[14:-1].split(' ')
            print(keystrokes)
            #if keystrokes[1] == 'up':
            #    keyboard.send(keystrokes[0])
            #elif keystrokes[1] == 'down':
            #    keystrokes.press(keystrokes[0])
                
client = Receiver()