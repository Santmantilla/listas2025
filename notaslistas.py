import os

alumnos = []
def agregar_alumno():
    global alumnos
    nombre = input("Ingrese el nombre del alumno: ")
    alumnos.append([nombre,[],[],[]])
def main_menu()-> int:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Menú de gestión de alumnos")
        print("1. Agregar alumno")
        print("2. Registrar notas")
        print("3. Consultar nota final")
        print("4. Salir")
        try:
            opcion = int(input("Seleccione una opción: "))
            if opcion < 1 or opcion > 4:
                print("Opción no válida. Intente de nuevo.")
                return main_menu()
            return opcion
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número.")
            return main_menu()
        
if __name__ == "__main__":
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Bienvenido al sistema de gestión de alumnos")
        opcion = main_menu()
        if opcion == 1:
            agregar_alumno()
        elif opcion == 2:
            pass
        elif opcion == 3:
            pass
        elif opcion == 4:
            os.system('pause')
            break
        else:
            print("Opción no válida. Intente de nuevo.")
