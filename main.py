from matriz import CMatFloat, crear_menu, leer_int

def main():
    matriz1 = CMatFloat()

    while True:
        print("\n=== MENÚ PRINCIPAL ===")
        opcion = crear_menu([
            "Construir matriz 1D",
            "Construir matriz 2D",
            "Introducir matriz",
            "Mostrar matriz",
            "Operaciones con matrices",
            "Terminar"
        ])

        if opcion == 1:
            n = leer_int("Número de elementos: ")
            matriz1.CrearMatriz1D(n)
        elif opcion == 2:
            f = leer_int("Número de filas: ")
            c = leer_int("Número de columnas: ")
            matriz1.CrearMatriz2D(f, c)
        elif opcion == 3:
            matriz1.Introducir()
        elif opcion == 4:
            matriz1.Mostrar()
        elif opcion == 5:
            operaciones_menu(matriz1)
        elif opcion == 6:
            print("Fin del programa.")
            break


def operaciones_menu(matriz1):
    while True:
        print("\n--- OPERACIONES CON MATRICES ---")
        opcion = crear_menu([
            "Sumar matrices",
            "Restar matrices",
            "Volver al menú principal"
        ])

        if opcion == 1 or opcion == 2:
            # Crear segunda matriz
            print("\nCrea la segunda matriz:")
            matriz2 = CMatFloat()
            f = matriz1._m_nFilas
            c = matriz1._m_nColumnas
            matriz2.CrearMatriz2D(f, c)
            matriz2.Introducir()

            if opcion == 1:
                resultado = matriz1.SumarMatrices(matriz2)
                if resultado is not None:
                    print("Resultado de la suma:")
                    print(resultado)
            elif opcion == 2:
                resultado = matriz1.RestarMatrices(matriz2)
                if resultado is not None:
                    print("Resultado de la resta:")
                    print(resultado)

        elif opcion == 3:
            break


if __name__ == "__main__":
    main()
