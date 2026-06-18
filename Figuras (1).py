# 2) Figuras geométricas (área)
from abc import ABC, abstractmethod  # Importa las herramientas para crear clases y métodos abstractos
import math  # Importa la librería matemática para poder usar el valor de Pi (pi)

class Figura(ABC):  # Define la clase abstracta 'Figura', que servirá de molde base
    @abstractmethod  # Declaración de que el siguiente método es abstracto y obligatorio para los hijos
    def area(self) -> float:  # Define la firma del método 'area' indicando que debe devolver un número decimal
        pass  # Marcador de posición que no realiza ninguna acción
        
    @abstractmethod  # Declaración de que el siguiente método también es abstracto y obligatorio
    def dibujar(self):  # Define la firma del método 'dibujar' sin implementar código todavía
        pass  # Marcador de posición que no realiza ninguna acción

class Circulo(Figura):  # Define la clase 'Circulo' que hereda todas las propiedades de 'Figura'
    def __init__(self, radio: float):  # Método constructor para el círculo que recibe el radio en formato decimal
        self.radio = radio  # Asigna y guarda el valor del radio recibido en los atributos del objeto
        
    def area(self) -> float:  # Implementa de forma obligatoria el cálculo del área para el círculo
        return math.pi * self.radio ** 2  # Calcula y devuelve el área usando la fórmula matemática: Pi * radio al cuadrado
        
    def dibujar(self):  # Implementa de forma obligatoria la acción de dibujar para el círculo
        print(f"Dibujando un círculo de radio {self.radio}")  # Imprime un mensaje en consola indicando el radio del círculo

class Rectangulo(Figura):  # Define la clase 'Rectangulo' que hereda todas las propiedades de 'Figura'
    def __init__(self, ancho: float, alto: float):  # Método constructor para el rectángulo que recibe ancho y alto
        self.ancho = ancho  # Guarda el valor del ancho recibido en el atributo correspondiente del objeto
        self.alto = alto  # Guarda el valor del alto recibido en el atributo correspondiente del objeto
        
    def area(self) -> float:  # Implementa de forma obligatoria el cálculo del área para el rectángulo
        return self.ancho * self.alto  # Calcula y devuelve el área multiplicando el ancho por la altura
        
    def dibujar(self):  # Implementa de forma obligatoria la acción de dibujar para el rectángulo
        print(f"Dibujando un rectángulo {self.ancho} x {self.alto}")  # Imprime en consola las dimensiones del rectángulo

class Triangulo(Figura):  # Define la clase 'Triangulo' que hereda todas las propiedades de 'Figura'
    def __init__(self, base: float, altura: float):  # Método constructor para el triángulo que recibe base y altura
        self.base = base  # Guarda el valor de la base recibida en el atributo correspondiente del objeto
        self.altura = altura  # Guarda el valor de la altura recibida en el atributo correspondiente del objeto
        
    def area(self) -> float:  # Implementa de forma obligatoria el cálculo del área para el triángulo
        return (self.base * self.altura) / 2  # Calcula y devuelve el área con la fórmula: (base * altura) dividido entre 2
        
    def dibujar(self):  # Implementa de forma obligatoria la acción de dibujar para el triángulo
        print(f"Dibujando un triángulo de base {self.base} y altura {self.altura}")  # Imprime en consola los datos del triángulo

def procesar_figura(figura: Figura):  # Define una función genérica que acepta cualquier objeto derivado de 'Figura'
    # Polimorfismo: misma interfaz, distintas implementaciones (Línea de comentario original de tu imagen)
    figura.dibujar()  # Llama al método 'dibujar' propio de la figura específica que se haya recibido
    print(f"Área = {figura.area():.2f}")  # Llama al método 'area', calcula el valor y lo imprime formateado a 2 decimales

if __name__ == "__main__":  # Evalúa si este archivo se está ejecutando directamente en el sistema
    figuras = [  # Declara e inicia una lista destinada a almacenar los objetos de las figuras geométricas
        Circulo(3),  # Crea un objeto 'Circulo' con radio 3 y lo añade a la lista de figuras
        Rectangulo(4, 5),  # Crea un objeto 'Rectangulo' con ancho 4 y alto 5, y lo añade a la lista
        Triangulo(6, 2)  # Crea un objeto 'Triangulo' con base 6 y altura 2, y lo añade a la lista
    ]  # Cierra correctamente la definición de la lista de figuras
    
    for f in figuras:  # Inicia un bucle para iterar sobre cada elemento 'f' guardado dentro de la lista 'figuras'
        procesar_figura(f)  # Envía la figura actual del ciclo a la función para ejecutar sus métodos compartidos
        print("-" * 20)  # Imprime una línea divisoria de 20 guiones en consola para separar los resultados