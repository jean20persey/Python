class Persona:
    total_personas = 0

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        Persona.total_personas += 1

    def saludar(self):
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años.")


class Estudiante(Persona):
    total_estudiantes = 0

    def __init__(self, nombre, edad, carrera):
        super().__init__(nombre, edad)
        self.carrera = carrera
        Estudiante.total_estudiantes += 1

    def imprimir_informacion(self):
        print(f"Nombre: {self.nombre}\nEdad: {self.edad}\nCarrera: {self.carrera}")


class Profesor(Persona):
    total_profesores = 00

    def __init__(self, nombre, edad, especialidad):
        super().__init__(nombre, edad)
        self.especialidad = especialidad
        Profesor.total_profesores += 1

    def imprimir_informacion(self):
        print(f"Nombre: {self.nombre}\nEdad: {self.edad}\nEspecialidad: {self.especialidad}")


# Ejemplo de uso
persona1 = Persona("Juan", 30)
persona1.saludar()

estudiante1 = Estudiante("Ana", 20, "Ingeniería")
estudiante1.imprimir_informacion()

profesor1 = Profesor("Carlos", 40, "Matemáticas")
profesor1.imprimir_informacion()

print(f"Total de personas: {Persona.total_personas}")
print(f"Total de estudiantes: {Estudiante.total_estudiantes}")
print(f"Total de profesores: {Profesor.total_profesores}")
