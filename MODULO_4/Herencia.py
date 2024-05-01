class Persona:
    def __init__(self,nombre,dni,edad,genero,nacionalidad) -> None:
        self.nombre = nombre
        self.dni = dni
        self.edad = edad
        self.genero = genero
        self.nacionalidad = nacionalidad
    
    def presentarse(self):
        print(f"Mi nombre es {self.nombre}, tengo {self.edad} años , y soy{self.nacionalidad}")
        
# al poner entre parentesis una clase , python automaticamente definra automaticamente esta como la clase padre / super class de la clase
class profesor(Persona):
    def __init__(self, nombre, dni, edad, genero, nacionalidad,tiempo_dictnado,curso,institucion) -> None:
        super().__init__(nombre, dni, edad, genero, nacionalidad)
        
        self.tiempo_trabajando_meses = tiempo_dictnado
        self.nombre_curso= curso
        self.nombre_institucion = institucion
    
    def presentacion_curso(self):
        print(f"-> Buenas tardes, mi nombre es {self.nombre}. Bienvenidos al curso de {self.nombre_curso}")

profesor_1= profesor("Gino quispe",123123123,23,"Masculino","Peruano",12,"Python para desarollo web","Plan San Marcos")
profesor_1.presentarse()
profesor_1.presentacion_curso()


persona_1 = Persona("Mathias Cabezas", 123124124,24,"Masculino","Peruano")
persona_1.presentarse()


print(Persona.__base__)
print(profesor.__base__)




        