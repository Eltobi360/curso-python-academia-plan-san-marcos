from abc import ABC, abstractclassmethod


class user(ABC):
    @abstractclassmethod
    def login():
        pass
    
    @abstractclassmethod
    def register(self):
        pass
    

class Customer(user):
    def __init__(self, nombre , email, password) -> None:
     self.nobre= nombre
     self.email= email
     self.password= password
     super().__init__()

    def login(self):
        print("se realizo el login correctamente")
    
    def register(self):
        print("Se registro correctamente")
        
class Admin(user_not_deprecated):
    def __init__(self, nombre,email,password):
            
    