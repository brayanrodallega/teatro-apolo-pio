import os
import pickle

# Función para crear la sala de cine
def crear_sala(filas, columnas):
    return [['O' for _ in range(columnas)] for _ in range(filas)]

# Función para mostrar la sala sin puestos ocupados (solo números)
def ver_sala_original(filas, columnas):
    contador = 1
    for i in range(filas):
        for j in range(columnas):
            print(f"{str(contador).ljust(2)}", end=' ')
            contador += 1
        print()

# Función para mostrar la sala con los puestos ocupados (indicados por un círculo púrpura)
def mostrar_sala(sala):
    filas = len(sala)
    columnas = len(sala[0])
    contador = 1
    for i in range(filas):
        for j in range(columnas):
            if sala[i][j] == 'X':
                print(f"\033[95m●\033[0m", end='  ')
            else:
                print(f"{str(contador).ljust(2)}", end=' ')
            contador += 1
        print()

# Función para reservar un asiento con numeración lineal
def reservar_asiento(sala, numero_asiento):
    try:
        filas = len(sala)
        columnas = len(sala[0])
        if 1 <= numero_asiento <= filas * columnas:
            fila = (numero_asiento - 1) // columnas
            columna = (numero_asiento - 1) % columnas
            if sala[fila][columna] == 'O':
                sala[fila][columna] = 'X'
                print(f"Su puesto asignado es: {numero_asiento}")
            else:
                print("El asiento ya está reservado.")
        else:
            print("Número de asiento inválido.")
    except Exception as e:
        print(f"Error al reservar asiento: {e}")

# Función para guardar la sala en un archivo usando pickle
def guardar_sala(sala, nombre_archivo="sala_cine.pkl"):
    try:
        with open(nombre_archivo, 'wb') as archivo:
            pickle.dump(sala, archivo)
        print(f"Sala guardada en {nombre_archivo}.")
    except Exception as e:
        print(f"Error al guardar la sala: {e}")

# Función para cargar la sala desde un archivo usando pickle
def cargar_sala(nombre_archivo="sala_cine.pkl"):
    try:
        if os.path.exists(nombre_archivo):
            with open(nombre_archivo, 'rb') as archivo:
                return pickle.load(archivo)
        else:
            print(f"No se encontró el archivo {nombre_archivo}.")
            return None
    except Exception as e:
        print(f"Error al cargar la sala: {e}")
        return None

# Función principal del programa
def main():
    try:
        nombre_archivo = "sala_cine.pkl"
        sala = cargar_sala(nombre_archivo)

        if sala is None:
            filas = int(input("Ingrese el número de filas: "))
            columnas = int(input("Ingrese el número de columnas: "))
            sala = crear_sala(filas, columnas)
        else:
            filas = len(sala)
            columnas = len(sala[0])

        while True:
            print("Menú:")
            print("1 - CREAR SALA")
            print("2 - VER SALA")
            print("3 - ASIGNAR PUESTO")
            print("4 - CARGAR SALA")
            print("5 - SALIR")
            opcion = input("Seleccione la opción deseada: ")

            if opcion == '1':
                filas = int(input("Ingrese el número de filas: "))
                columnas = int(input("Ingrese el número de columnas: "))
                sala = crear_sala(filas, columnas)
            elif opcion == '2':
                ver_sala_original(filas, columnas)
            elif opcion == '3':
                numero_asiento = int(input("Ingrese el número de asiento que desea reservar: "))
                reservar_asiento(sala, numero_asiento)
            elif opcion == '4':
                mostrar_sala(sala)
            elif opcion == '5':
                guardar_sala(sala, nombre_archivo)
                break
            else:
                print("Opción no válida. Intente nuevamente.")
    except Exception as e:
        print(f"Error en el programa principal: {e}")

if __name__ == "__main__":
    main()
