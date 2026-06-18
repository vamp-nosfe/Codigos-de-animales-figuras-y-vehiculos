# 3) Vehículos y movimientos:
# Importa los módulos necesarios para definir clases abstractas en Python.
from abc import ABC, abstractmethod

# Define la clase base abstracta de la cual heredarán los vehículos.
class Vehiculo(ABC):
    # Constructor de la clase que inicializa el atributo de la marca.
    def __init__(self, marca: str):
        # Asigna el valor del parámetro marca al atributo del objeto.
        self.marca = marca
    
    # Declara el método abstracto para obligar a las clases hijas a usarlo.
    @abstractmethod
    def arrancar(self):
        # Se usa 'pass' ya que los métodos abstractos no llevan lógica aquí.
        pass
    
    # Declara un segundo método abstracto que también debe ser obligatorio.
    @abstractmethod
    def moverse(self):
        # Indica que la implementación real se definirá en las subclases.
        pass

# Define la clase Auto que hereda directamente de la clase Vehiculo.
class Auto(Vehiculo):
    # Implementa de forma específica el método de arranque para un auto.
    def arrancar(self):
        # Muestra en pantalla el mensaje de arranque usando la marca del auto.
        print(f"Auto {self.marca} arrancando con llave.")
    
    # Implementa de forma específica el método de movimiento para un auto.
    def moverse(self):
        # Muestra en pantalla cómo se desplaza este vehículo en particular.
        print(f"Auto {self.marca} circulando por la carretera.")

# Define la clase Moto que hereda las propiedades de la clase Vehiculo.
class Moto(Vehiculo):
    # Define la acción de arrancar adaptada a las características de una moto.
    def arrancar(self):
        # Imprime el mensaje correspondiente al encendido eléctrico de la moto.
        print(f"Moto {self.marca} arrancando con botón eléctrico.")
    
    # Define la acción de moverse según el comportamiento de una moto.
    def moverse(self):
        # Muestra el mensaje informativo sobre el avance de la moto en el tráfico.
        print(f"Moto {self.marca} avanzando entre el tráfico.")

# Define la clase Camion que hereda el comportamiento base de Vehiculo.
class Camion(Vehiculo):
    # Establece la forma en que un camión realiza su proceso de arranque.
    def arrancar(self):
        # Muestra un mensaje en consola sobre el encendido del motor diésel.
        print(f"Camión {self.marca} encendiendo motor diésel.")

    # Establece la manera en que un camión ejecuta su desplazamiento.
    def moverse(self):
        # Imprime la descripción del traslado de carga pesada del camión.
        print(f"Camión {self.marca} transportando carga pesada.")

# Función global encargada de gestionar el viaje de cualquier tipo de vehículo.
def iniciar_viaje(vehiculo: Vehiculo):
    # # Polimorfismo: misma llamada, diferente comportamiento
    # Llama al método arrancar del objeto recibido sin importar su clase específica.
    vehiculo.arrancar()
    # Llama al método moverse aplicando la lógica del objeto que corresponda.
    vehiculo.moverse()

# Verifica si el archivo se está ejecutando directamente como programa principal.
if __name__ == "__main__":
    # Inicializa una lista que almacenará las distintas instancias de vehículos.
    flota = [
        # Crea un objeto de la clase Auto con la marca Toyota.
        Auto("Toyota"),
        # Crea un objeto de la clase Moto con la marca Yamaha.
        Moto("Yamaha"),
        # Crea un objeto de la clase Camion con la marca Volvo.
        Camion("Volvo")
    ]
    
    # Inicia un bucle para recorrer uno a uno los elementos de la lista.
    for v in flota:
        # Ejecuta las acciones de viaje para el vehículo que está en turno.
        iniciar_viaje(v)
        # Imprime una línea de guiones para separar visualmente cada vehículo.
        print("-" * 20)