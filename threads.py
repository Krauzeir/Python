from threading import Thread
import time

class Produtor1(Thread):

    def __init__(self):
        super().__init__()
        
        self.numero = 0
        self.continuar = True
    
    def parar(self):
        self.continuar = False
        
    def get_numero(self):
        return self.numero
    
    def run(self):
        while self.continuar:
            self.numero = self.numero + 1

class Produtor2(Thread):
    
    def __init__(self):
        super().__init__()
        
        self.numero = 0
        self.continuar = True
    
    def parar(self):
        self.continuar = False
        
    def get_numero(self):
        return self.numero
    
    def run(self):
        while self.continuar:
            self.numero = self.numero + 1
            
            time.sleep(2)
            
if __name__ == '__main__':
    produtor1 = Produtor1()
    produtor2 = Produtor2()
    
    produtor1.start()
    produtor2.start()
    
    for i in range(10):
        print("numero do produtor 1: ", produtor1.get_numero())
        print("numero do produtor 2: ", produtor2.get_numero())
        
        time.sleep(1)
    
    produtor1.parar()
    produtor2.parar()
    
    time.sleep(3)
    
    