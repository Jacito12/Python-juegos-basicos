import random

def palabras_secretas() -> str:
    print("---------------------------------")
    print("Bienvenido al juego del ahorcado")
    print("---------------------------------")
    print("Los temas son los siguientes: ")
    print("1. Platos peruanos :P")
    print("2. Países del mundo :D")
    print("3. Razas de perros :D")

    while True:
        tema = input("Elige un tema (1, 2 o 3): ")
        if tema == "1":
            return random.choice(["ceviche", "lomo saltado", "aji de gallina", "rocoto relleno", "anticuchos", "causa limeña", "pollo a la brasa"])
        elif tema == "2":
            return random.choice(["perú", "argentina", "colombia", "ecuador", "venezuela", "brasil", "méxico", "españa", "francia", "japón"])
        elif tema == "3":
            return random.choice(["pug", "pastor alemán", "labrador", "bulldog", "chihuahua", "dálmata", "golden retriever", "husky siberiano", "beagle", "boxer"])
        else:
            print("Opción no válida. Por favor, elige 1, 2 o 3.")

def mostrar_progreso(palabra_secreta, letras_adivinadas):
    progreso = []
    for letra in palabra_secreta:
        if letra == ' ':
            progreso.append(' ')  # Mostrar espacios directamente
        elif letra in letras_adivinadas:
            progreso.append(letra)
        else:
            progreso.append('_')
    return ' '.join(progreso)  # Separar letras con espacios para mejor visualización

def juego_ahorcado():
    palabra_secreta = palabras_secretas()
    letras_adivinadas = set()
    intentos = 6
    juego_terminado = False

    print(f"\n¡Comenzemos con el juego B)")
    print(f"La palabra a adivinar es: {mostrar_progreso(palabra_secreta, letras_adivinadas)}")
    print(f"Tienes {intentos} intentos para adivinar la palabra.")

    while not juego_terminado and intentos > 0:
        letra = input("\nIngresa una letra: ").lower()
        if len(letra) != 1 or not letra.isalpha():
            print("Por favor, ingresa una letra válida.")
        elif letra in letras_adivinadas:
            print("Ya adivinaste esa letra. Intenta con otra.")
        else:
            letras_adivinadas.add(letra)
            if letra not in palabra_secreta:
                intentos -= 1
                print(f"La letra '{letra}' no está en la palabra. Te quedan {intentos} intentos.")
            else:
                print(f"Bien ahi B) La letra '{letra}' está en la palabra.")

            progreso_actual = mostrar_progreso(palabra_secreta, letras_adivinadas)
            print(progreso_actual)

            if '_' not in progreso_actual:
                juego_terminado = True
                print("\n¡Felicidades! Has adivinado la palabra:", palabra_secreta)

    if intentos == 0:
        print("\nLo siento, has agotado tus intentos. La palabra era:", palabra_secreta)

juego_ahorcado()