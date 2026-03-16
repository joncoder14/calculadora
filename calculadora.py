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
                            medida = input("ingrese la unidad de medidad en EEUU")
                            if perimetro > 0 and apotema > 0:
                                
                                area = (perimetro * apotema) / 2
                                print("el area es:", area, medida)
                                h = False
                            else:
                                print("error no puedes poner numeros negativos y tine que se mayor a cero")
                        except:
                            print("ingrese valor valido")
                    elif oph == 2:
                        try:
                            print("para hallar el perimetro necesito que me de un lado")
                            lado = float(input("ingrese el lado en entero o decimal: "))
                            medida = input("ingrese la unidad de medidad en EEUU")
                            if lado > 0:
                                perimetro = 6 * lado
                                print("el perimetro es:", perimetro, medida)
                                h = False
                            else:
                                print("error no puedes ingresar numeros igual o menores a cero")
                        except:
                            print("ingrese valor valido")
                    elif oph == 3:
                        try:
                            print("para hacer este calculo necesito que ingrese el lado")
                            lado = float(input("ingrese lado: "))
                            medida = input("ingrese la unidad de medidad en EEUU")
                            if lado > 0:
                                apotema = (3**(1/2))/2 * lado
                                print("la apotema es:", apotema, medida)
                                h = False
                            else:
                                print("error no puedes ingresear numeros menores o igual a cero")
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
                            if a1 > 0 and a2 > 0:
                                suma_angulos = a1 + a2
                                if suma_angulos < 180: 
                                    angulo = 180 - suma_angulos
                                    print("el angulo es:", angulo,"°")
                                    t = False
                                else:
                                    print("los datos de los angulos no coiciden")
                            else:
                                print("error no puedes ingresar numeros igual o menores a cero")
                        except:
                            print("invalido intenta de nuevo")
                    elif opt == 2:
                        print("para esto necesito saber la base y la altura")
                        try:
                            base = float(input("ingrese la base: "))
                            altura = float(input("ingrese la altura: "))
                            medida = input("ingrese la unidad de medidad en EEUU")
                            if base > 0 and altura > 0:
                                area = base * altura / 2
                                print("el area es:", area, medida)
                                t = False
                            else:
                                print("error no puedes ingresar numeros igual o menores a cero")
                        except:
                            print("invalido intenta de nuevo")
                    elif opt == 3:
                        print("para saber la altura necesito saber la base y el area")
                        try:
                            area = float(input("ingrese el area: "))
                            base = float(input("ingrese la base: "))
                            medida = input("ingrese la unidad de medidad en EEUU")
                            if area > 0 and base >0:
                                altura = (2 * area) / base
                                print("la altura del triangulo es:", altura, medida)
                                t = False
                            else:
                                print("error no puedes ingresar numeros igual o menores a cero")
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
                            medida = input("ingrese la unidad de medidad en EEUU")
                            if perimetro > 0 and apotema > 0:
                                area = perimetro * apotema / 2
                                print("el area es:", area, medida)
                                p = False
                            else:
                                print("error no puedes ingresar numeros igual o menores a cero")
                        except:
                            print("invalido intenta de nuevo")
                    elif opp == 2:
                        print("para hacer este calculo necesito saber la longitud de un lado")
                        try:
                            lado = float(input("ingrese la longitud de un lado: "))
                            medida = input("ingrese la unidad de medidad en EEUU")
                            if lado > 0:
                                perimetro = lado * 5
                                print("el perimetro es:", perimetro, medida)
                                p = False
                            else:
                                print("error no puedes ingresar numeros igual o menores a cero")
                        except:
                            print("invalido intenta de nuevo")
                    elif opp ==3:
                        print("para hacer esta operacion necesito saber el area y el perimetro")
                        try:
                            area = float(input("ingrese el area: "))
                            perimetro = float(input("ingrese el perimetro: "))
                            medida = input("ingrese la unidad de medidad en EEUU")
                            if area >0 and perimetro >0:
                                apotema = (2 * area)/perimetro
                                print("la apotema es:", apotema, medida)
                                p = False
                            else:
                                print("error no puedes ingresar numeros igual o menores a cero")
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
                            medida = input("ingrese la unidad de medidad en EEUU")
                            if d_mayor > 0 and d_menor > 0:
                                area = (d_mayor * d_menor) / 2
                                print("el area es:", area, medida)
                                r = False
                            else:
                                print("error no puedes ingresar numeros igual o menores a cero")
                        except:
                            print("invalido intenta de nuevo")
                    elif opr == 2:
                        print("para hacer este calculo necesito saber la longitud de un lado")
                        try:
                            longitud = float(input("ingrese la longitud de un lado: "))
                            medida = input("ingrese la unidad de medidad en EEUU")
                            if longitud > 0:
                                perimetro = 4 * longitud
                                print("el perimetro es:", perimetro, medida)
                                r = False
                            else:
                                print("error no puedes ingresar numeros igual o menores a cero")
                        except:
                            print("invalido intenta de nuevo")
                    elif opr ==3:
                        print("para saber la altura necesito el area y un lado")
                        try:
                            area = float(input("ingresa el area: "))
                            lado = float(input("ingrese un lado: "))
                            medida = input("ingrese la unidad de medidad en EEUU")
                            if lado > 0 and area > 0:
                                altura = area / lado
                                print("la altura es:", altura, medida)
                                r = False
                            else:
                                print("error no puedes ingresar numeros igual o menores a cero")
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
                            medida = input("ingrese la unidad de medidad en EEUU")
                            if base_triangulo > 0 and altura_triangulo > 0:
                                area_base = (base_triangulo * altura_triangulo) / 2
                                print("el area de la base es:", area_base, medida)
                                pt = False
                            else:
                                print("error no puedes ingresar numeros igual o menores a cero")
                            
                        except:
                            print("invalido intente nuevo")
                    elif oppt == 2:
                        print("para hallar el perimetro de la base debo saber los tres lados del triangulo ")
                        try:
                            l_1 = float(input("ingrese el lado 1: "))
                            l_2 = float(input("ingrese el lado 2: "))
                            l_3 = float(input("ingrese el lado 3: "))
                            medida = input("ingrese la unidad de medidad en EEUU")

                            if l_1 > 0 and l_2 > 0 and l_3 > 0:
                                perimetro_base = l_1 + l_2 + l_3
                                print("el perimetro de la base es:", perimetro_base, medida)
                                pt = False
                            else:
                                print("error no puedes ingresar numeros igual o menores a cero")
                        except:
                            print("invalido intente nuevo")
                    elif oppt ==3:
                        print("para saber el volumen necesito saber el area de la base y la altura del prisma ")
                        try:
                            area_base = float(input("ingrese el area de la base: "))
                            altura_prisma = float(input("ingrese la altura del prisma: "))
                            medida = input("ingrese la unidad de medidad en EEUU")
                            if area_base >0 and altura_prisma > 0:
                                volumen = area_base * altura_prisma
                                print("el volumen es:", volumen, medida)
                                pt = False
                            else:
                                print("error no puedes ingresar numeros igual o menores a cero")
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
                    pi = 3.1416
                    radio = float(input("ingrese el radio del cilindro: "))
                    medida = input("ingrese la unidad de medidad en EEUU")
                    if radio > 0:
                        if opc == 1:
                            try:
                                altura = float(input("ingrese la altura del cilindro: "))
                                medida = input("ingrese la unidad de medidad en EEUU debe ser igual a la de radio")
                                if altura > 0:
                                    volumen = pi * radio **2 * altura
                                    print("el volumen es:", volumen, medida)
                                    c = False
                                else:
                                    print("error no puedes ingresar numeros igual o menores a cero")
                            except:
                                print("error intenta de nuevo")
                        elif opc == 2:
                            area_base = pi * radio ** 2
                           
                            print("el area de la base es:", area_base, medida)
                            c = False
                        elif opc ==3:
                            perimetro_base = 2 * pi * radio
                           
                            print("perimetro de la base:", perimetro_base, medida)
                            c = False
                    else:
                        print("el radio debe ser mayro a cero")
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
                    pi = 3.1416
                    ope = int(input("ingrese la opcion que desea: "))
                    radio = float(input("ingrese el radio de la circunferencia: "))
                    medida = input("ingrese la unidad de medidad en EEUU")
                    if radio > 0:

                        if ope == 1:
                            area_esfera = 4 * pi * radio **2
                          
                            print("el area de la esfera es:", area_esfera, medida)
                            e = False
                        elif ope == 2:
                            volumen = (4/3) * pi * radio **3
                           
                            print("el volumen de la esfera es:", volumen, medida)
                            e = False
                        elif ope == 3:
                            circunferencia_max = 2 * pi * radio
                            
                            print("la circunferencia es:", circunferencia_max, medida)
                            e = False
                        elif ope == 4:
                            try:
                                altura = float(input("ingrese la altura: "))
                                medida = input("ingrese la unidad de medidad en EEUU debe ser igual a la del radio")
                                if altura > 0:
                                    casquete = 2 * pi * radio * altura
                                    print("el area del casquete es:", casquete, medida)
                                    e = False
                                else:
                                    print("error no puedes ingresar numeros igual o menores a cero")
                            except:
                                print("invalido intenta de nuevo")
                    else:
                        print("el radio debe ser mayor a cero")
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
                    pi = 3.1416
                    opco = int(input("ingrese lo que desea hallar: "))
                    radio = float(input("ingrese el radio del cono: "))
                    medida = input("ingrese la unidad de medidad en EEUU")
                    if radio > 0:
                        if opco ==1:
                            try:
                                altura = float(input("ingrese la altura: "))
                                medida = input("ingrese la unidad de medidad en EEUU debe ser la misma que la de radio")
                                if altura > 0:
                                    volumen = (1/3) * pi * radio **2 * altura
                                    print("el volumen es:", volumen, medida)
                                    co = False
                                else:
                                    print("error no puedes ingresar numeros igual o menores a cero")
                            except:
                                print("invalido intenta de nuevo")
                        elif opco == 2:
                            area_base = pi * radio**2
                            print("el area de la base es:", area_base, medida)
                            co = False
                        elif opco == 3:
                            try:
                                generatriz = float(input("ingrese el generatriz del cono: "))
                                medida = input("ingrese la unidad de medidad en EEUU debe ser la misma que la de radio")
                                if generatriz > 0:
                                    area_total = pi * radio * (radio + generatriz)
                                    print("el area total es:", area_total, medida)
                                    co = False
                                else:
                                    print("error no puedes ingresar numeros igual o menores a cero")
                            except:
                                print("invalido intenta de nuevo")
                    else:
                        print("el radio debe ser mayor a cero")
                except:
                    print("invalido intenta de nuevo")

        elif opcion == 9:
            print("""bien has elegido el triangulo rectangulo
                1.hipotenusa
                2.cateto adyacente
                3.cateto opuesto
                4.angulo
                 """)
            tr = True
            while tr:
                try: 
                    optr = int(input("ingrese la opcion que desea hallar: "))
                    if optr == 1:
                        try:
                            cateto_a = float(input("ingrese el cateto adyacente: "))
                            cateto_o = float(input("ingrese el cateto opuesto: "))
                            medida = input("ingrese la unidad de medidad en EEUU")
                            if cateto_a > 0 and cateto_o >0:
                                hipotenusa = (cateto_a *2 + cateto_o **2) * (1/2)
                                print("la hipotenusa del triangulo rectangulo es:", hipotenusa, medida)
                                tr = False
                            else:
                                print("error no puedes ingresar numeros igual o menores a cero")
                        except:
                            print("invalido intenta de nuevo")
                    elif optr == 2:
                        try:
                            cateto_o = float(input("ingrese el cateto opuesto: "))
                            hipotenusa = float(input("ingrese la hipotenusa: "))
                            medida = input("ingrese la unidad de medidad en EEUU")
                            if cateto_o and hipotenusa > 0:
                                cateto_a = (hipotenusa *2 - cateto_o **2) *(1/2)
                                print("el cateto adyacente es:", cateto_a, medida)
                                tr = False
                            else:
                                print("error no puedes ingresar numeros igual o menores a cero")
                        except:
                            print("invalido intenta de nuevo")
                    elif optr == 3:
                        try:
                            cateto_a = float(input("ingrese el cateto adyacente: "))
                            hipotenusa = float(input("ingrese la hipotenusa: "))
                            medida = input("ingrese la unidad de medidad en EEUU")
                            if cateto_a >0 and hipotenusa > 0:
                                cateto_o = (hipotenusa*2 - cateto_a *2) *(1/2)
                                print("el cateto opuesto es:", cateto_o, medida)
                                tr = False
                            else:
                                print("error no puedes ingresar numeros igual o menores a cero")
                        except: 
                            print("invalido intenta de nuevo")
                    elif optr == 4:
                        try:
                            a1 = float(input("ingrese el angulo uno: "))
                            a2 = float(input("ingrese el angulo dos: "))
                            if a1 > 0 and a1 == 90 or a2 > 0 and a2 == 90:
                                suma_angulos = a1 + a2
                                if suma_angulos <= 179.9: 
                                    angulo = 180 - (a1 + a2)
                                    print("el angulo es:", angulo,"°")
                                    tr = False
                                else:
                                    print("error no puedes ingresar numeros igual o menores a cero")
                            else:
                                print("error no puedes ingresar numeros igual o menores a cero")
                                print("un angulo debe medir 90 grados ya que es un angulo rectangulo")
                        except:
                            print("invalido intenta de nuevo")                   
                except: 
                    print("invalido intenta de nuevo")

        elif opcion == 10:
            print("saliendo...")
            op = False  

    except:
        print("invalido intenta de nuevo")
            





        