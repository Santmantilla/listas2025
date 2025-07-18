import os
equipos = []
fechas = [[],[[],[]],[[],[]]]

def main_menu()-> int:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("-------------------------------------------")
        print("|----- BIENVENIDO A LA LIGA BETPLAY ------|")
        print("|-----------------------------------------|")
        print("|1. Registrar equipo                      |")
        print("|2. Programar fecha                       |")
        print("|3. Registrar marcador                    |")
        print("|4. Equipo con mas goles en contra        |")
        print("|5. Equipo con mas goles a favor          |")
        print("|6. Registro plantel                      |")
        print("|7. Salir                                 |")
        print("-------------------------------------------")
        try:
            opcion = int(input("Seleccione una opción: "))
            if opcion < 1 or opcion > 7:
                print("Opción no válida. Intente de nuevo.")
                os.system('pause')
                return main_menu()
            return opcion
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número.")
            os.system('pause')
            return main_menu()
        
def registrar_equipo():
    global equipos 
    nombreEquipo = input('Ingrese el nombre del equipo: ').lower()
    equipos.append([nombreEquipo,[[],[],[],[],[],[]],[],[],[],[],[],[[],[],[],[]],[[],[]]])

""" def registrar_puntos(nombreEquipo):
    try:
        partidosGanados = int(input(f'Ingrese los partidos ganados de {equipos}'))
        if(partidosGanados >= 0):
            return partidosGanados
        else:
            print('No puedes ingresar numeros negativos')
    except ValueError:
        print("Por favor, ingrese un número válido.") """



if __name__ == "__main__":
    while True:
        opcion = main_menu()
        if opcion == 1:
            registrar_equipo()
            print(equipos)
            print(f'Equipo agregado con éxito.')
            input('Presione Enter para continuar...')
        elif opcion == 2:
            pass
        elif opcion == 3:
            pass
        elif opcion == 4:
            break
        else:
            print("Opción no válida. Intente de nuevo.")





