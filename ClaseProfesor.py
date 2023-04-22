
from abc import ABC, abstractmethod #SE IMPORTA la biblioteca "abc" para definir clases abstractas y métodos abstractos

#SE CREA LA CLASE ProfeEstudiante con los métodos esta sera la clase padre
class ProfeEstudiante(ABC):
    @abstractmethod
    def Cedula(self, cedula):
        pass

    @abstractmethod
    def Nombre(self, nombre):
        pass

    @abstractmethod
    def fechaNacimiento(self, fechaNacimiento):
        pass

    @abstractmethod
    def nCelular(self, nCelular):
         pass
#SE CREA CLASE PROFESOR que es una clase hija que hereda los metodos de la clase Profestudiante
class Profesor(ProfeEstudiante):

    # constructor de la clase
    def _init_(self, cedula, nombre, fechaNacimiento, nCelular):  # ATRIBUTOS DE LA CLASE
        self.cedula = cedula  # CEDULA DEL PROFESOR
        self.nombre = nombre  # NOMBRE DEL PROFESOR
        self.fechaNacimiento = fechaNacimiento  # FECHA DE NACIMIENTO DEL PROFESOR
        self.nCelular = nCelular  # NUMERO DE CELULAR DEL PROFESOR