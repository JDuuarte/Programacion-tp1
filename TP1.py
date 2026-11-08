#Solamente hasta clase 6. Se puede hacer con bucles, listas, match, condicionales, random. NO ENTRAN FUNCIONES. 

puntaje = 100
apuesta_defecto = 10
contador = 0
i = True
import random
caracteres = ["A", "B", "C", "D", "7", "0"]
caracteres_aleatorios = []

while i == True :

    print("*" * 50)
    print()
    print("1. Jugar (apuesta por defecto: 10 puntos)")
    print("2. Cambiar apuesta")
    print("3. Salir")
    print()
    print("*" * 50)
    print()

    opcion = input("Selecciona una opcion: ")
    print("-" * 50)
    print()
    match opcion:

        case "1":
            if puntaje >= 10:

                print("Apostando 10 puntos")
                print()
                
                while contador < 3:
                         
                    azar = random.randint(0,5)
                    caracteres_aleatorios += [caracteres[azar]]
                    contador += 1
                
            valor_uno = caracteres_aleatorios[0]
            valor_dos = caracteres_aleatorios[1]
            valor_tres = caracteres_aleatorios[2]

            print("TU RESULTADO:")

            for j in caracteres_aleatorios:
                print(j, end= "  ")
            
            print()
            
            # REGLA 1: Tres caracteres "0" (pierde todo y termina)
            if valor_uno == "0" and valor_dos == "0" and valor_tres == "0":

                print("El resultado fue triple 0, perdes tus puntos y finaliza el juego.")
                puntaje = 0
                i = False

            # REGLA 2: Tres caracteres "7" (gana 10 veces)
            elif valor_uno == "7" and valor_dos == "7" and valor_tres == "7":

                print("Felicitaciones! Tu puntaje se multiplico por 10")
                premio = apuesta_defecto * 10
                puntaje += premio
                print("Tu puntaje es:", puntaje)
                print()

            # REGLA 3: Tres caracteres iguales de A, B, C o D (gana 5 veces)
            elif valor_uno == valor_dos and valor_dos == valor_tres:

                print("Felicitaciones! Tres iguales, tu puntaje se multiplico por 5")
                premio = apuesta_defecto * 5
                puntaje += premio
                print("Tu puntaje es:", puntaje)
                print()

            # REGLA 4: Dos caracteres iguales (gana 2 veces)
            elif valor_uno == valor_dos or valor_uno == valor_tres or valor_dos == valor_tres:
                print("Felicitaciones! Dos iguales, tu puntaje se multiplico por 2")
                premio = apuesta_defecto * 2
                puntaje += premio
                print("Tu puntaje es:", puntaje)
                print()
                
            # REGLA 5: Todos distintos (pierde la apuesta)
            else:
                print("Lo siento! Todos distintos, perdiste tu apuesta")
                puntaje -= apuesta_defecto
                print("Tu puntaje es:", puntaje)
                print()
            
        case "2":
            apueta_cambiada = int(input("Indicar monto a apostar: "))
        
            while apueta_cambiada < 0 or apueta_cambiada > puntaje:
                apueta_cambiada = int(input("Ingresa un monto correcto para apostar: "))

                print("Apostando 10 puntos")
                print()
                
            while contador < 3:
                         
                azar = random.randint(0,5)
                caracteres_aleatorios += [caracteres[azar]]
                contador += 1
                
            valor_uno = caracteres_aleatorios[0]
            valor_dos = caracteres_aleatorios[1]
            valor_tres = caracteres_aleatorios[2]

            print("TU RESULTADO:")

            for j in caracteres_aleatorios:
                print(j, end= "  ")
            
            print()
            
            # REGLA 1: Tres caracteres "0" (pierde todo y termina)
            if valor_uno == "0" and valor_dos == "0" and valor_tres == "0":

                print("El resultado fue triple 0, perdes tus puntos y finaliza el juego.")
                puntaje = 0
                i = False

            # REGLA 2: Tres caracteres "7" (gana 10 veces)
            elif valor_uno == "7" and valor_dos == "7" and valor_tres == "7":

                print("Felicitaciones! Tu puntaje se multiplico por 10")
                premio = apueta_cambiada * 10
                puntaje += premio
                print("Tu puntaje es:", puntaje)
                print()

            # REGLA 3: Tres caracteres iguales de A, B, C o D (gana 5 veces)
            elif valor_uno == valor_dos and valor_dos == valor_tres:

                print("Felicitaciones! Tres iguales, tu puntaje se multiplico por 5")
                premio = apueta_cambiada * 5
                puntaje += premio
                print("Tu puntaje es:", puntaje)
                print()

            # REGLA 4: Dos caracteres iguales (gana 2 veces)
            elif valor_uno == valor_dos or valor_uno == valor_tres or valor_dos == valor_tres:
                print("Felicitaciones! Dos iguales, tu puntaje se multiplico por 2")
                premio = apueta_cambiada * 2
                puntaje += premio
                print("Tu puntaje es:", puntaje)
                print()
                
            # REGLA 5: Todos distintos (pierde la apuesta)
            else:
                print("Lo siento! Todos distintos, perdiste tu apuesta")
                puntaje -= apueta_cambiada
                print("Tu puntaje es:", puntaje)
                print()


        case "3":
            i = False
            if puntaje > 0:
                print("Te retiraste con un saldo de:", puntaje)
            
            else:
                Print("Saliendo...")

        case _:
            print("Seleccionaste una opcion incorrecta")

    contador = 0
    caracteres_aleatorios = []

