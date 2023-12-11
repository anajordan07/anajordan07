from random import randit
aleatorio=randit(1,100)
#Variable de control para salir del bucle
control=0
#Almacenarmos el número de intentos
intentos=0
while intentos<10 and control==0:
    numero=int(input("Numero"))
    intentos=intentos+1
    if numero<aleatorio:
        print("Debes introdeucir un número mayor")
    else:
        if numero<aleatrio:
            print("Debes introducir un número numero")
        else:
            print("Acertaste en", intentos,"intentos")
            control=1
if control==0:
    print("Esto no es lo tuyo !!")
