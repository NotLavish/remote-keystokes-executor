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
        
        self.ip = socket.gethostname()
        self.port = 2222
        
        self.s.connect((self.ip, int(self.port)))
        
        self.username = 'recv'
        self.s.send(self.username.encode())
        
        print(f"u da {self.username}")
        
        input_handler = threading.Thread(target=self.input_handler,args=())
        input_handler.start()
        
    def input_handler(self):
        isPaused = False
        while True:
            msg = self.s.recv(5024).decode()
            keystrokes = msg.split(" ")
            key = keystrokes[-2].split("(")[-1]
            if key == "esc":
                if isPaused:
                    isPaused = False
                else:
                    isPaused = True
            if isPaused:
                pass
            else:
                if keystrokes[-1][:-1] == 'up':
                    keyboard.release(key)
                elif keystrokes[-1][:-1] == 'down':
                    keyboard.press(key)
                
client = Receiver()