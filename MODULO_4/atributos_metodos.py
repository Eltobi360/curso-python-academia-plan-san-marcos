class CuentaBancaria:
    #atributo de la clase
    interes = 0.06
    #contructor :
    def __init__(self,nombre , correro , dni) -> None:
        self.nombre_usuario = nombre
        self.correro_usuario= correro
        self.dni_usuario = dni
        pass

Cuenta_Bancaria_1 = CuentaBancaria("Alexander","alexanderpatinoQgmail.com","75121312")
Cuenta_Bancaria_2 = CuentaBancaria("Gino","gquispec@gmail.com","751213123")
print(Cuenta_Bancaria_1.correro_usuario)
print(Cuenta_Bancaria_1.interes)

print(Cuenta_Bancaria_2.correro_usuario)
print(Cuenta_Bancaria_2.interes)

CuentaBancaria_3 = CuentaBancaria(nombre= "Matias", correro="matias@gmail.com",dni="12345678")



class Perro: 
    
    #__init__ es un  parametro
    
    __cansancio = 0
    def __init__(self,nobmre,edad,raza,peso) -> None:
        self.nombre= nobmre
        self.edad= edad
        self.raza= raza
        self.peso= peso
    
    #funciones
    
    #Metodo correr
    def correr(self, distancia= float):
        if self.__cansancio> 50:
            print(f"{self.nombre} esta cansado. No puede correr por ahora")
        else:  
            print(f"{self.nombre} esta corriendo {distancia} km.")
            self.__cansancio +=50

    def descanso(self, horas_descanso = int):
        if horas_descanso>=6:
            self.__resetear_cansancio()
        if horas_descanso <=5:
            self.__cansancio -= (horas_descanso * 10)
        else:
            print(f"{self.nombre} no duerme mas de 5 horas")
            
    def __resetear_cansancio(self):
        self.__cansancio = 0
fido = Perro(nobmre="Fido", edad= 4, raza="Pitbull", peso=10)
print(fido.nombre)
fido.correr(10.5)
fido.correr(10.5)
fido.descanso(4)
fido.correr(5)
print(fido.__cansancio)

peluchin = Perro(nobmre="Peluchin", edad= 14, raza="shitsu", peso=7)

print(peluchin.cansancio)