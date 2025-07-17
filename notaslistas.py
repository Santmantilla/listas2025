import os
alumnos = []
def agregar_alumno():
    global alumnos
    nombre = input("Ingrese el nombre del alumno: ").strip().lower()
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
    if(len(alumno[1]) >= 3):
        print('No puedes ingresar mas de 3 notas')
        os.system('pause')
    else:
        nota = pedir_nota('Parcial')
        alumno[1].append(nota)

def registro_quiz(alumno):
    if(len(alumno[2]) >= 4):
        print('No puedes ingresar mas de 4 notas')
        os.system('pause')
    else:
        nota = pedir_nota('Quiz')
        alumno[2].append(nota)


def registro_trabajo(alumno):
    if(len(alumno[3]) >= 2):
        print('No puedes ingresar mas de 2 notas')
        os.system('pause')
    else:
        nota = pedir_nota('Trabajo')
        alumno[3].append(nota)
    
def registro_notas():
    nombre = input('Ingrese el nombre del alumno al que le registrara la nota: ').strip().lower()
    for i in alumnos:
        if(i[0].lower() == nombre):
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

def notas_final():
    nombre = input('Ingrese el nombre del alumno del que quiere ver la nota final: ').strip().lower()
    for i in alumnos:
        if(i[0] == nombre):
            parciales = i[1]
            quices = i[2]
            trabajos = i[3]

            if (len(parciales) != 3 or len(quices) != 4 or len(trabajos) != 2):
                print('No estan todas las notas registradas.')
            else:
                todas = parciales + quices + trabajos
                promedio = round(sum(todas) / len(todas),2)
                print(f'La nota final de {nombre} es: {promedio}')
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
            notas_final()
            os.system('pause')
        elif opcion == 4:
            break
        else:
            print("Opción no válida. Intente de nuevo.")
