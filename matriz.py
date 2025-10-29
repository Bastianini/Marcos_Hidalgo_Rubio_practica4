import numpy as np

class CMatFloat:
    """
    Clase que representa una matriz dinámica 1D/2D.
    """

    def __init__(self):
        """Inicializa la matriz vacía."""
        self._Matriz = None
        self._m_nFilas = 0
        self._m_nColumnas = 0

    def CrearMatriz2D(self, nFilas, nColumnas):
        """Crea una matriz bidimensional de ceros."""
        self._Matriz = np.zeros((nFilas, nColumnas), dtype=float)
        self._m_nFilas = nFilas
        self._m_nColumnas = nColumnas

    def CrearMatriz1D(self, nElementos):
        """Crea una matriz unidimensional (vector fila)."""
        self.CrearMatriz2D(1, nElementos)

    def Introducir(self):
        """Introduce los elementos de la matriz desde teclado."""
        if not self.Existe():
            print("No hay ninguna matriz creada.")
            return
        for i in range(self._m_nFilas):
            for j in range(self._m_nColumnas):
                self._Matriz[i][j] = leer_float(f"Elemento [{i},{j}]: ")

    def Mostrar(self):
        """Muestra la matriz."""
        if not self.Existe():
            print("No hay ninguna matriz creada.")
            return
        print("Contenido de la matriz:")
        print(self._Matriz)

    def Existe(self):
        """Verifica si la matriz existe y tiene elementos."""
        return self._Matriz is not None and self._Matriz.size > 0

    def SumarMatrices(self, otra_matriz):
        """Suma dos matrices del mismo tamaño."""
        if not (self.Existe() and otra_matriz.Existe()):
            print("Alguna de las matrices no está creada.")
            return None
        if self._Matriz.shape != otra_matriz._Matriz.shape:
            print("Error: Las dimensiones deben coincidir.")
            return None
        return self._Matriz + otra_matriz._Matriz

    def RestarMatrices(self, otra_matriz):
        """Resta dos matrices del mismo tamaño."""
        if not (self.Existe() and otra_matriz.Existe()):
            print("Alguna de las matrices no está creada.")
            return None
        if self._Matriz.shape != otra_matriz._Matriz.shape:
            print("Error: Las dimensiones deben coincidir.")
            return None
        return self._Matriz - otra_matriz._Matriz


# --- Funciones auxiliares ---

def leer_int(mensaje="Introduce un número entero: "):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Valor no válido. Inténtalo de nuevo.")

def leer_float(mensaje="Introduce un número decimal: "):
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Valor no válido. Inténtalo de nuevo.")

def crear_menu(opciones_menu):
    """Muestra un menú y devuelve la opción elegida."""
    for i, opcion in enumerate(opciones_menu, 1):
        print(f"{i}. {opcion}")
    while True:
        opcion = leer_int("Selecciona una opción: ")
        if 1 <= opcion <= len(opciones_menu):
            return opcion
        print("Opción no válida, inténtalo de nuevo.")
