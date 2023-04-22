#se importan la clase profesor y la clase estudiante

from ClaseProfesor import Profesor
from ClaseEstudiante import Estudiante
#se crea clase factory matricula
class FactoryMatricula:

    # se crea metodo factory para retornar un objeto de la clase
    # Instancia de la clase que va a retornar sea de tipo profesor o estudiante de las clase creadas
    def CrearProEst(self, tipo):
        if tipo == 'profesor':
            return Profesor()
        elif tipo == 'Estudiante':
            return Estudiante()
        else:
          None