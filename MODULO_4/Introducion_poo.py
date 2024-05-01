numero=20
#20 que es literal -> es una instancia de la clase int

print(type(numero))
#la variable nombre almacena un objeto str
nombre="Jorge"
print(type(nombre))
print(nombre.upper())

#print(nombre.__dir__())

#creando la primera clase

class estudiante:
    #atributo
    nacionalidad ="Peruana"
    #contructor
    def __init__(self, nombre,apellido,edad,curso,documento_indentidad):
        self.nombre=nombre
        self.apellido=apellido
        self.edad=edad
        self.curso=curso
        self.documento_indentidad=documento_indentidad
    #metodos
    def realizar_examen(self):
        print(f"{self.nombre} El estudiante esta realizando el examen")
    def mirar_clase(self):
        print(f"El alumno registrado con documento : {self.documento_indentidad} ")

estudiante_1=estudiante("Jorge","Mauricio",20,"Pytohn para desarrollo",8123812)

print(estudiante_1.nombre)
estudiante_1.realizar_examen()
estudiante_1.mirar_clase()
print(type(estudiante_1))