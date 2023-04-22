from ClaseProfesor import ProfeEstudiante # se importa claseProfesor y clase Profeestudiante
# Clase Estudiante que guarda la información de los estudiantes de la institución
class Estudiante(ProfeEstudiante): # SE CREA CLASE ESTUDIANTE QUE HEREDA DE LA CLASE metodos de la clase Profestudiante

    #constructor de la clase estudiante
    def _init_(self, cedula, nombre, fechaNacimiento, nCelular, grupo): #ATRIBUTOS DE LA CLASE
        self.cedula = cedula  # CEDULA DEL ESTUDIANTE
        self.nombre = nombre  # NOMBRE DEL ESTUDIANTE
        self.fechaNacimiento = fechaNacimiento  # FECHA DE NACIMIENTO DEL ESTUDIANTE
        self.nCelular = nCelular  # NUMERO DE CELULAR DEL ESTUDIANTE
        self.grupo = grupo  # GRUPO/CLASeDELESTUDIANTE