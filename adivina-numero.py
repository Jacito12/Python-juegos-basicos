import random

def adivinar_numero():
    numero_secreto = random.randint(1,100)
    intentos = 0
    adivinaste = False

    print("--------------------------------------")
    print("Adivina un número entre el 1 y el 100")
    print("--------------------------------------")
    print("Suerte!! :D")

    while not adivinaste:
        numero_ingreso = input("Introduce el número: ")
        if not numero_ingreso.isdigit():
            print("No ingresaste un número D: vuelve a intentarlo! ")
        elif ( int(numero_ingreso) < 1 or int(numero_ingreso) > 100 ):
            print("Te saliste del rango de números!!! vuelve a intentarlo :D")
        else :
            numero_ingreso = int(numero_ingreso)
            intentos+=1
            if numero_ingreso > numero_secreto:
                print(f"El número que debes adivina es menor a {numero_ingreso}. Inténtalo de nuevo :D")
            elif numero_ingreso < numero_secreto:
                print(f"El número que debes adivina es mayor a {numero_ingreso}. Inténtalo de nuevo :D")

            else:
                print(f"Felicidades!! :D, el número era {numero_secreto}.")
                print(f"Lo haz logrado en {intentos} intentos.") 
                adivinaste = True

adivinar_numero()