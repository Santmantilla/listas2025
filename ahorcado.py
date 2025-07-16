import random
import os
palabras = ['python', 'programacion', 'desarrollo', 'algoritmo', 'funcion']
def elegir_palabra():
    return random.choice(palabras)
def jugar_ahorcado():
    palabra = elegir_palabra()
    letras_adivinadas = []
    intentos = 3
    while intentos > 0:

        os.system('cls' if os.name == 'nt' else 'clear')
        print("\nPalabra\n", " ".join([letra if letra in letras_adivinadas else "_" for letra in palabra]))
        print("Letras adivinadas:", " ".join(letras_adivinadas))
        print(f"Intentos restantes: {intentos}")

        letra = input("Adivina una letra: ").lower()
        if letra in letras_adivinadas:
            print("Ya has adivinado esa letra.😂")
            os.system('pause')
            continue
        letras_adivinadas.append(letra)
        if letra not in palabra:
            intentos -= 1
            print("Letra incorrecta.🤬")
            os.system('pause')
        else:
            print("¡Bien hecho!")
        if all(letra in letras_adivinadas for letra in palabra):
            print(f"¡Felicidades! Has adivinado la palabra: {palabra}")
            return
    print(f"Has perdido🤮. La palabra era: {palabra}")
    
print("¡Bienvenido al juego del ahorcado!")
jugar_ahorcado()  # Inicia el juego del ahorcado