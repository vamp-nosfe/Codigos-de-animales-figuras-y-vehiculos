# 1) Animales y sonido:
from abc import ABC, abstractmethod  # Importa las herramientas para crear clases abstractas y métodos abstractos

class Animal(ABC):  # Define la clase abstractas 'Animal', que sirve de molde para otras clases
    def __init__(self, nombre):  # Define el método constructor que se ejecuta al crear un objeto
        self.nombre = nombre  # Guarda el nombre recibido en un atributo propio del objeto
        
    @abstractmethod  # Indica que el siguiente método es abstracto y DEBE ser obligatorio en los hijos
    def hacer_sonido(self):  # Define la firma del método 'hacer_sonido' sin implementar su lógica
        pass  # Palabra clave que no hace nada, usada como marcador de posición

class Perro(Animal):  # Define la clase 'Perro' que hereda (es subclase) de la clase 'Animal'
    def hacer_sonido(self):  # Implementa obligatoriamente el método 'hacer_sonido' para el perro
        return f"{self.nombre} dice: Guau!"  # Devuelve una cadena con el nombre del perro y su ladrido

class Gato(Animal):  # Define la clase 'Gato' que hereda (es subclase) de la clase 'Animal'
    def hacer_sonido(self):  # Implementa obligatoriamente el método 'hacer_sonido' para el gato
        return f"{self.nombre} dice: Miau!"  # Devuelve una cadena con el nombre del gato y su maullido

class Pajaro(Animal):  # Define la clase 'Pajaro' que hereda (es subclase) de la clase 'Animal'
    def hacer_sonido(self):  # Implementa obligatoriamente el método 'hacer_sonido' para el pájaro
        return f"{self.nombre} dice: Pío pío!"  # Devuelve una cadena con el nombre del pájaro y su canto

def reproducir_sonido(animal: Animal):  # Define una función que recibe un objeto que debe ser de tipo 'Animal'
    # Polimorfismo: el mismo método se comporta distinto según la subclase (Línea de comentario original)
    print(animal.hacer_sonido())  # Llama al método del objeto y muestra el resultado en la consola

if __name__ == "__main__":  # Evalúa si este archivo se está ejecutando directamente como el programa principal
    animales = [  # Declara e inicia una lista que contendrá las instancias de los animales
        Perro("Firulais"),  # Crea un objeto de la clase 'Perro' llamado "Firulais" y lo añade a la lista
        Gato("Misu"),  # Crea un objeto de la clase 'Gato' llamado "Misu" y lo añade a la lista
        Pajaro("Piolín")  # Crea un objeto de la clase 'Pajaro' llamado "Piolín" y lo añade a la lista
    ]  # Cierra la definición de la lista de animales
    
    for a in animales:  # Inicia un ciclo para recorrer cada elemento 'a' dentro de la lista 'animales'
        reproducir_sonido(a)  # Envía el animal actual a la función para que imprima su sonido respectivo