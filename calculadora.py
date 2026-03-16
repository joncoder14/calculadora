print("""hola bienvenido a esta calculadora geometrica donde puedes hallar cosas de diferentes figuras:
      1.hexagono
      2.triangulo
      3.pentagono
      4.rombo
      5.piramide
      6.cilindro
      7.esfera
      8.cono
      9.triangulo rectangulo
      10.salir""")

op = True
while op:
    try:
        opcion = int(input("ingrese el numero de la figura que desea: "))
        if opcion == 1:
            print("""bien elegiste hexagono, puedes elegir las siguientes opciones:
                  1.hallar area
                  2.hallar perimetro
                  3.apotema
                  """)
            h = True
            while(h):
                try:
                    oph = int(input("ingrese el numero de la opcion que desea: "))
                    if oph == 1:
                        try:
                            print("para hacer este calculo necesito que ingrese el perimetro y el apotema")
                            perimetro = float(input("ingrese el perimetro: "))
                            apotema = float(input("ingrese la apotema en entero o decimal: "))
                            area = (perimetro * apotema) / 2
                            print("el area es:", area)
                            h = False
                        except:
                            print("ingrese valor valido")
                    elif oph == 2:
                        try:
                            print("para hallar el perimetro necesito que me de un lado")
                            lado = float(input("ingrese el lado en entero o decimal: "))
                            perimetro = 6 * lado
                            print("el perimetro es:", perimetro)
                            h = False
                        except:
                            print("ingrese valor valido")
                    elif oph == 3:
                        try:
                            print("para hacer este calculo necesito que ingrese el lado")
                            lado = float(input("ingrese lado: "))
                            apotema = (3**(1/2))/2 * lado
                            print("la apotema es:", apotema)
                            h = False
                        except:
                            print("ingrese una opcion valida")
                except:
                    print("invalido por favor intenta con un valor valido")

        elif opcion == 2:
            print("""bien elegiste triangulo que deseas hallar ?
            1.angulo
            2.area
            3.altura""")
            t = True
            while t:
                try:
                    opt = int(input("ingrese la opcion que desea: "))
                    if opt == 1:
                        print("para saber un angulo necesito que ingrese dos angulos")
                        try:
                            a1 = float(input("ingrese el angulo uno: "))
                            a2 = float(input("ingrese el angulo dos: "))
                            angulo = 180 - (a1 + a2)
                            print("el angulo es:", angulo)
                            t = False
                        except:
                            print("invalido intenta de nuevo")
                    elif opt == 2:
                        print("para esto necesito saber la base y la altura")
                        try:
                            base = float(input("ingrese la base: "))
                            altura = float(input("ingrese la altura: "))
                            area = base * altura / 2
                            print("el area es:", area)
                            t = False
                        except:
                            print("invalido intenta de nuevo")
                    elif opt == 3:
                        print("para saber la altura necesito saber la base y el area")
                        try:
                            area = float(input("ingrese el area: "))
                            base = float(input("ingrese la base: "))
                            altura = (2 * area) / base
                            print("la altura del triangulo es:", altura)
                            t = False
                        except:
                            print("invalido intenta de nuevo")
                except:
                    print("invalido intenta de nuevo")

        elif opcion == 3:
            print("""bien elegiste pentagono que desea hallar ?
            1.area
            2.perimetro
            3.apotema""")
            p = True
            while p:
                try:
                    opp = int(input("ingrese una opcion: "))
                    if opp == 1:
                        print("para hacer este calculo necesito saber el perimetro y la apotema")
                        try:
                            perimetro = float(input("ingrese el perimetro: "))
                            apotema = float(input("ingresa la apotema: "))
                            area = perimetro * apotema / 2
                            print("el area es:", area)
                        except:
                            print("invalido intenta de nuevo")
                    elif opp == 2:
                        print("para hacer este calculo necesito saber la longitud de un lado")
                        try:
                            lado = float(input("ingrese la longitud de un lado: "))
                            perimetro = lado * 5
                            print("el perimetro es:", perimetro)
                            p = False
                        except:
                            print("invalido intenta de nuevo")
                    elif opp ==3:
                        print("para hacer esta operacion necesito saber el area y el perimetro")
                        try:
                            area = float(input("ingrese el area: "))
                            perimetro = float(input("ingrese el perimetro: "))
                            apotema = (2 * area)/perimetro
                            print("la apotema es:", apotema)
                            p = False
                        except:
                            print("invalido intenta de nuevo")
                except:
                    print("invalido intenta de nuevo")

        elif opcion == 4:
            print("""bien elegiste rombo que desea hallar ?
            1.area
            2.perimetro
            3.altura""")
            r = True
            while r:
                try:
                    opr = int(input("ingrese una opcion: "))
                    if opr == 1:
                        print("para hacer esto necesito saber la diagonal mayor y la diagonal menor")
                        try:
                            d_mayor = float(input("ingrese la diagonal mayor: "))
                            d_menor = float(input("ingrese la diagonal menor: "))
                            area = (d_mayor * d_menor) / 2
                            print("el area es:", area)
                            r = False
                        except:
                            print("invalido intenta de nuevo")
                    elif opr == 2:
                        print("para hacer este calculo necesito saber la longitud de un lado")
                        try:
                            longitud = float(input("ingrese la longitud de un lado: "))
                            perimetro = 4 * longitud
                            print("el perimetro es:", perimetro)
                            r = False
                        except:
                            print("invalido intenta de nuevo")
                    elif opr ==3:
                        print("para saber la altura necesito el area y un lado")
                        try:
                            area = float(input("ingresa el area: "))
                            lado = float(input("ingrese un lado: "))
                            altura = area / lado
                            print("la altura es:", altura)
                        except:
                            print("intenta de nuevo")
                except:
                    print("invalido intenta de nuevo")

        elif opcion == 5:
            print("""bien elegiste prisma triangular que desea hallar ?
            1.area de la base
            2.perimetro de la base
            3.volumen""")
            pt = True
            while pt:
                try:
                    oppt = int(input("ingrese una opcion: "))
                    if oppt == 1:
                        print("para calcular el area de la base necesito saber base del triangulo y la altura del triangulo (perpendicular a la base)")
                        try:
                            base_triangulo = float(input("ingrese la base del triangulo: "))
                            altura_triangulo = float(input("ingrese la altura de la base: "))
                            area_base = (base_triangulo * altura_triangulo) / 2
                            print("el area de la base es:", area_base)
                            pt = False
                        except:
                            print("invalido intente nuevo")
                    elif oppt == 2:
                        print("para hallar el perimetro de la base debo saber los tres lados del triangulo ")
                        try:
                            l_1 = float(input("ingrese el lado 1: "))
                            l_2 = float(input("ingrese el lado 2: "))
                            l_3 = float(input("ingrese el lado 3: "))
                            perimetro_base = l_1 + l_2 + l_3
                            print("el perimetro de la base es:", perimetro_base)
                            pt = False
                        except:
                            print("invalido intente nuevo")
                    elif oppt ==3:
                        print("para saber el volumen necesito saber el area de la base y la altura del prisma ")
                        try:
                            area_base = float(input("ingrese el area de la base: "))
                            altura_prisma = float(input("ingrese la altura del prisma: "))
                            volumen = area_base * altura_prisma
                            print("el volumen es:", volumen)
                            pt = False
                        except:
                            print("invalido intenta de nuevo")
                except:
                    print("invalido intenta de nuevo")

        elif opcion == 6:
            print("""bien elegiste el cilindro que desea hallar ?
            1.volumen
            2.area de la base
            3.Perímetro de la base (circunferencia)""")
            c = True
            while c:
                try:
                    opc = int(input("ingrese una opcion: "))
                    radio = float(input("ingrese el radio del cilindro: "))
                    pi = 3.1416
                    if opc == 1:
                        try:
                            altura = float(input("ingrese la altura del cilindro: "))
                            volumen = pi * radio **2 * altura
                            print("el volumen es:", volumen)
                            c = False
                        except:
                            print("error intenta de nuevo")
                    elif opc == 2:
                        area_base = pi * radio ** 2
                        print("el area de la base es:", area_base)
                        c = False
                    elif opc ==3:
                        perimetro_base = 2 * pi * radio
                        print("perimetro de la base:", perimetro_base)
                        c = False
                except:
                    print("invalido intenta de nuevo")

        elif opcion == 7:
            print("""bien elegiste esfera que deseas hallar ?
            1.area de la esfera
            2.volumen
            3.circunferencia del circulo maximo
            4.area de un casquete esferico""")
            e = True
            while e:
                try:
                    ope = int(input("ingrese la opcion que desea: "))
                    radio = float(input("ingrese el radio de la circunferencia: "))
                    pi = 3.1416

                    if ope == 1:
                        area_esfera = 4 * pi * radio **2
                        print("el area de la esfera es:", area_esfera)
                        e = False
                    elif ope == 2:
                        volumen = (4/3) * pi * radio **3
                        print("el volumen de la esfera es:", volumen)
                        e = False
                    elif ope == 3:
                        circunferencia_max = 2 * pi * radio
                        print("la circunferencia es:", circunferencia_max)
                        e = False
                    elif ope == 4:
                        try:
                            altura = float(input("ingrese la altura: "))
                            casquete = 2 * pi * radio * altura
                            print("el area del casquete es:", casquete)
                            e = False
                        except:
                            print("invalido intenta de nuevo")
                except:
                    print("invalido intenta de nuevo")

        elif opcion == 8:
            print("""bien elegiste cono
                1.volumen
                2.area de la base
                3.area total""")
            co = True
            while co:
                try:
                    opco = int(input("ingrese lo que desea hallar: "))
                    radio = float(input("ingrese el radio del cono: "))
                    pi = 3.1416
                    if opco ==1:
                        try:
                            altura = float(input("ingrese la altura: "))
                            volumen = (1/3) * pi * radio **2 * altura
                            print("el volumen es:", volumen)
                            co = False
                        except:
                            print("invalido intenta de nuevo")
                    elif opco == 2:
                        area_base = pi * radio**2
                        print("el area de la base es:", area_base)
                        co = False
                    elif opco == 3:
                        try:
                            generatriz = float(input("ingrese el generatriz del cono: "))
                            area_total = pi * radio * (radio + generatriz)
                            print("el area total es:", area_total)
                            co = False
                        except:
                            print("invalido intenta de nuevo")
                except:
                    print("invalido intenta de nuevo")

        elif opcion == 9:
            print("""bien has elegido el triangulo rectangulo
                1.hipotenusa
                2.cateto adyacente
                3.cateto opuesto
                 """)
            tr = True
            while tr:
                try: 
                    optr = int(input("ingrese la opcion que desea hallar: "))
                    if optr == 1:
                        try:
                            cateto_a = float(input("ingrese el cateto adyacente: "))
                            cateto_o = float(input("ingrese el cateto opuesto: "))
                            hipotenusa = (cateto_a *2 + cateto_o **2) * (1/2)
                            print("la hipotenusa del triangulo rectangulo es:", hipotenusa)
                            tr = False
                        except:
                            print("invalido intenta de nuevo")
                    elif optr == 2:
                        try:
                            cateto_o = float(input("ingrese el cateto opuesto: "))
                            hipotenusa = float(input("ingrese la hipotenusa: "))
                            cateto_a = (hipotenusa *2 - cateto_o **2) *(1/2)
                            print("el cateto adyacente es:", cateto_a)
                            tr = False
                        except:
                            print("invalido intenta de nuevo")
                    elif optr == 3:
                        try:
                            cateto_a = float(input("ingrese el cateto adyacente: "))
                            hipotenusa = float(input("ingrese la hipotenusa: "))
                            cateto_o = (hipotenusa*2 - cateto_a2) *(1/2)
                            print("el cateto opuesto es:", cateto_o)
                            tr = False
                        except: 
                            print("invalido intenta de nuevo")

                except: 
                    print("invalido intenta de nuevo")

        elif opcion == 10:
            print("saliendo...")
            op = False  

    except:
        print("invalido intenta de nuevo")
            





        