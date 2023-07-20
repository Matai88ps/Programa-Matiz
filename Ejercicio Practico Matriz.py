"""Empezamos con while para que el programa no se pare 
cuando introduciomos valores no permitidos"""

while True:
    
    try:
   
        # Tamaño matriz.
        N = int(input("Introduce el tamaño de tu Matriz: "))

        # En el caso que introduzcan un 0.
        if N == 0:
            print("El valor " ,N, " no genera una matriz, por favor introduce un valor mayor de 0. ")
            N = []
            continue

        else:
            # Si introducen un numero negativo.
            if N < 0:
                print("El valor " ,N, " es menor que 0, por favor introduce un valor mayor de 0. ")
                N = []
                continue

            else:
                # Crear matriz
                import random
                matriz = []
                for i in range(N):
                    matriz.append([])
                    for j in range(N):
                        matriz[i].append(random.randint(0, 9))

                # Mostrando en pantalla la matiz.
                print("La matriz " ,N,"x",N, "es la siguiente: ")
                for i in matriz:
                    a = str(i)[1:-1]
                    print(a.ljust(0, " "))

                # Suma de las filas de la matriz.
                suma_filas = []
                for i in matriz:
                    suma_filas.append(sum(i))

                # Impresion de la suma sin corchetes.
                print("La suma de cada fila es: ")
                b = str(suma_filas)[1:-1]
                print(b.ljust(0, " "))

                # Suma de las columnas de la matriz.
                suma_coltotal = []
                for j in range(N):
                    suma_columnas = 0
                    for i in range(N):
                        suma_columnas += matriz[i][j]
                    suma_coltotal.append(suma_columnas)

                # Impresion de la suma sin corchetes.
                print("La suma de cada columna es: ")
                c = str(suma_coltotal)[1:-1]
                print(c.ljust(0, " "))
                N = []
                break

    # Excepcion cuando introduzcan una letra, simbolo o decimales.
    except ValueError:
        print("El valor introducido no es un numero entero.")
        continue
