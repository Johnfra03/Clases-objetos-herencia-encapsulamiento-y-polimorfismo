# Clase base: Persona
class Persona:
    """
    Clase base que representa una persona con atributos comunes como nombre y edad.
    """
    def __init__(self, nombre, edad):
        self.nombre = nombre  # Atributo público
        self._edad = edad  # Atributo protegido (no debe ser modificado directamente)

    def mostrar_informacion(self):
        """
        Método para mostrar información básica de una persona.
        """
        return f"Nombre: {self.nombre}, Edad: {self._edad}"

    def saludo(self):
        """
        Método que puede ser sobrescrito por clases derivadas.
        """
        raise NotImplementedError("Este método debe ser implementado en una subclase.")

# Clase derivada: Estudiante
class Estudiante(Persona):
    """
    Clase que hereda de Persona y añade atributos y métodos específicos para estudiantes.
    """
    def __init__(self, nombre, edad, numero_matricula, asignatura):
        super().__init__(nombre, edad)  # Llamada al constructor de la clase base
        self.numero_matricula = numero_matricula  # Atributo específico de Estudiante
        self.asignatura = asignatura  # Atributo específico de Estudiante

    def mostrar_informacion(self):
        """
        Sobrescritura del método para incluir información del estudiante.
        """
        info_base = super().mostrar_informacion()
        return f"{info_base}, Matrícula: {self.numero_matricula}, Asignatura: {self.asignatura}"

    def saludo(self):
        """
        Implementación del método saludo para estudiantes.
        """
        return f"Hola, soy {self.nombre} y estoy inscrito en la asignatura de {self.asignatura}."

# Clase derivada con encapsulación: Profesor
class Profesor(Persona):
    """
    Clase que hereda de Persona y añade atributos y métodos específicos para profesores.
    """
    def __init__(self, nombre, edad, materia_especialidad):
        super().__init__(nombre, edad)  # Llamada al constructor de la clase base
        self.__materia_especialidad = materia_especialidad  # Atributo privado (encapsulado)

    def mostrar_informacion(self):
        """
        Sobrescritura del método para incluir información del profesor.
        """
        info_base = super().mostrar_informacion()
        return f"{info_base}, Especialidad: {self.__materia_especialidad}"

    def obtener_especialidad(self):
        """
        Método público para acceder al atributo privado __materia_especialidad.
        """
        return self.__materia_especialidad

    def saludo(self):
        """
        Implementación del método saludo para profesores.
        """
        return f"Hola, soy el profesor {self.nombre} y enseño {self.__materia_especialidad}."

# Creación de instancias de las clases
estudiante1 = Estudiante("John Franco", 25, "12345", "Programación")
profesor1 = Profesor("Luis Cola", 35, "Programación")

# Uso de métodos y atributos
print(estudiante1.mostrar_informacion())  # Información del estudiante
print(estudiante1.saludo())  # Saludo del estudiante

print(profesor1.mostrar_informacion())  # Información del profesor
print(profesor1.saludo())  # Saludo del profesor

# Acceso al atributo privado del profesor usando un método público
print(f"La especialidad de {profesor1.nombre} es: {profesor1.obtener_especialidad()}")
