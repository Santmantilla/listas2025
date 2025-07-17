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
                os.system('pause')
                return main_menu()
            return opcion
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número.")
            os.system('pause')
            return main_menu()
        
def main_menu_calificaciones()-> int:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Menú de calificaciones")
        print("1. Registrar parciales")
        print("2. Registrar quices")
        print("3. Registrar trabajos")
        print("4. Salir")
        try:
            opcion = int(input("Seleccione una opción: "))
            if opcion < 1 or opcion > 4:
                print("Opción no válida. Intente de nuevo.")
                os.system('pause')
                return main_menu_calificaciones()
            return opcion
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número.")
            os.system('pause')
            return main_menu_calificaciones()
        
def pedir_nota(tipo):
    while True:
        try:
            nota = int(input(f"Ingrese la nota del {tipo}: "))
            if (nota <= 100):
                return nota
            else:
                print("El rango de notas es de 0 a 100")
        except ValueError:
            print("Por favor, ingrese un número válido.")
        
def registro_parcial(alumno):
    nota1 = pedir_nota('Parcial #1')
    nota2 = pedir_nota('Parcial #2')
    nota3 = pedir_nota('Parcial #3')
    alumno[1].append(nota1)
    alumno[1].append(nota2)
    alumno[1].append(nota3)

def registro_quiz(alumno):
    nota = pedir_nota('Quiz')
    alumno[2].append(nota)

def registro_trabajo(alumno):
    nota = pedir_nota('Trabajo')
    alumno[3].append(nota)
    
def registro_notas():
    nombre = input('Ingrese el nombre del alumno al que le registrara la nota: ')
    for i in alumnos:
        if(i[0] == nombre):
            while True:
                opcion2 = main_menu_calificaciones()
                match opcion2:
                    case 1:
                        registro_parcial(i)
                    case 2:
                         registro_quiz(i)
                    case 3:
                        registro_trabajo(i)
                    case 4:
                        return
                    case _:
                        break
    else:
        print(f"El alumno '{nombre}' no está registrado.")
        os.system('pause')                


if __name__ == "__main__":
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Bienvenido al sistema de gestión de alumnos")
        opcion = main_menu()
        if opcion == 1:
            agregar_alumno()
            print(f'Alumno agregado con éxito.')
            os.system('pause')
        elif opcion == 2:
            registro_notas()
            print(alumnos)
            os.system('pause')
        elif opcion == 3:
            pass
        elif opcion == 4:
            os.system('pause')
            break
        else:
            print("Opción no válida. Intente de nuevo.")
