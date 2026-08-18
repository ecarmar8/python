#nombre = (input("Ingrese el nombre del jugador: "))
#edad = int(input("Ingrese su edad: "))
#if edad < 4:
#    print(f"Hola {nombre}, por tu edad juegas gratis.")
#elif edad > 4 and edad <= 18:
#    print(f"Hola {nombre}, debes pagar $10.000.")
#elif edad > 18:
#    print(f"Hola {nombre}, debes pagar $20.000.")


    # Otra forma de hacerlo
nombre = (input("Ingrese el nombre del jugador: "))
edad = int(input("Ingrese su edad: "))
if edad < 4:  
    precio = 0
elif edad <= 18:
    precio = 10000
else:
    precio = 20000
print(f"Hola {nombre}, debes pagar ${precio}.")