class user:
    __is_login =False
    #s
    def __init__(self,email,name,password) -> None:
        self.user_name=name
        self.user_email=email
        self.password=password
        
        
    def wa_login(self):
        if self.__is_login == True:
            print("El usuario ya a tenido una secion iniciada anteriormente")
            return True
    #inicio de cesion
    def login(self,username,password):
        #peticion a internet / request -> se espera a una respuesta (response)
        if self.wa_login() == True or (self.user_name == username and self.password == password):
            print("se inicio bien")
            self.__is_login = True
        else:
            print("las credenciales son invalidadas")
            self.__is_login = False
    def show_products(self):
        if self.__is_login == True:
            print(f"Los productos recomendados para el usuario {self.user_name} son :")
            print("Lista de productos...")
        else:
            print("El usuario no ha iniciado sesion")
            
            
user_jorge= user("mneyraarzapalo@gmail.com","Jorge","contraseña")




user_jorge.login("Jorge","contraseña")
user_jorge.show_products()