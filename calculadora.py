print("""hola vienvenido a esta calculadora geometrica donde puedes hallar cosas de diferentes figuras: 
      1.hexagono
      2.triangulo
      3.pentagono
      4.rombo
      5.cubo
      6.cilindro
      7.esfera
      8.cono
      9.triangulo rectangulo
      10.salir""")
op = True
while op:
    try:
        opcion = int(input("ingrese el numero de la figura que desea "))
        if opcion == 1:
            print("""bien elegiste hexagono, puedes eligir las siguientes opciones:
                  1.hallar area
                  2.hallar perimetro
                  3.apotema
                  """)
            h = True
            while(h):
                try:
                    oph = int(input("ingrese el numero de la opcion que desea "))
                    if oph == 1:
                        try:
                            print("para hacer este calculo necesito que ingrese el perimetro y el apotema")
                            perimetro = float(input("ingrese el perimetro"))
                            apotema = float(input("ingrese la apotema en entero o decimal"))
                            area = (perimetro * apotema) / 2
                            print("el area es: ",area)
                            h = False
                        except:
                            print("ingrese valor valido")
                    elif oph == 2:
                        try:    
                            print("para hallar el perimetro necesito que me de un lado")
                            lado = float(input("ingrese el lado en entero o decimal"))
                            perimetro = 6 * lado
                            print(perimetro)
                            h = False
                        except:
                            print("ingrese valor valido")
                    elif oph == 3:
                        try:
                            print("para hacer este calculo necesito que ingrese el lado")
                            lado = float(input("ingrese lado"))
                            apotema = (3**(1/2))/2 * lado
                            h = False
                        except:
                            print("ingrese una opcion valida")
                except:
                    print("invalido por favor intenta con un valor valido")
        elif opcion == 2:
            





        