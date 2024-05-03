class User:
    def __init__(self, email, password, username) -> None:
        self.email = email
        self.password = password
        self.username = username
    def singIn(self):
        pass
    
class Admin(User):
    
    __admin_mail = "admin@gmail.com"
    __admin_password = "admin"
    __type_users_admin = {1:"Full administrador", 2: "Administrador de BD", 3: "Administrador de publicaciones"}
    __securyti_token=""
    def __init__(self, email, password, username, type_user) -> None:
        super().__init__(email, password, username)
        self.type_user = type_user
        
    def __validate_token(self) -> bool:
        return True if len(self.__securyti_token) == 0 else False
    def singIn(self):
        if (self.email == self.__admin_mail and 
            self.password == self.__admin_password 
            and self.type_user in self.__type_users_admin()): # se pude encapusular las condicionales con un parentecis para evitar que el codigo se aga tena largo
            self.__securyti_token == "asdasdasdjljlk2j421480421412qwedfhdsfhkjsdhfu1u2h"
            
    def manage_bd(self):
        if self.__validate_token():
            print("el usuario puede acceder a manejar la base de datos")
        elif self.type_user != 2:
            print("el usuario administrador no tiene los permisos para esta funcionalidad")
        else:
            print("credenciales incorrectas")
    def manage_posta(self):
        if self.__validate_token and self.type_user != 3:
            print("este usuario puede acceder a manejar la base de datos")
        elif self.type_user != 2:
            print("este usuario administrador no tiene los permisos para esta funcionalidad")
        else:
            print("credenciales incorrectas")
            