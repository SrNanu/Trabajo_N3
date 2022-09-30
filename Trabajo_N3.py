
import opcode
from operator import truediv
from string import ascii_letters
import platform
import os

"""
TYPE
productos disponibles = array [0..4] of tring
productos elegidos = array [0..2] of tring
datos de cupos tipo string = array bidimensional [0..7] [0..2] of string
datos de cupos tipo enteros = array bidimensional [0..7] [0..2] of integer

VAR
mayor, menor, cant_camio, cant, p, pos, i, j, limp, newp, cl, n_producto, peso_bruto, tara = enteros
p_mayor, p_menor, opcion_menu, opcion_opcion, opcion_admi, patente = string
proddis = productos disponibles
producto = productos elegidos
cupos = datos de cupos tipo string
cupos_numeros = datos de cupos tipo entero


"""


#inicializacion de variables
cant_camio = 0
producto = [" "] *3 #cuando termine poner [" "]*3
cant=0
proddis = ["TRIGO", "SOJA", "MAIZ", "GIRASOL", "CEBADA"]
p = 0
pos = -1
cupos = [" "]*8
cupos_numeros = [0]*8
for i in range (0,8):
    cupos [i] = [" "]* 3
    
for i in range (0,8):
    cupos_numeros [i] = [0]* 3
    
def mostrar_lista(lista,tamaño):
    for i in range(0,tamaño):
        print ("[", i, "]",lista[i])
def buscar_lista(lista,tamaño,b):
    for i in range(0,tamaño):
        if lista[i] == b:
            return True
    return False
def buscar_encupos(p,col):
    for i in range (0,8):
        if cupos [i][col] == p:
            return True
    return False
def buscar_posicion(array,tamaño, busca):
    for i in range (0,tamaño):
        if array [i][0] == busca:
            return i
    return -1
def estado_camion(p):
    for i in range (0,8):
        if cupos[i][0] == p:
            return cupos [i][1]
    return "no"
def es_patente(patente):
    if (len(patente) == 6 or len(patente) == 7)  and patente.isalnum():
        return True
    else: 
        return False
def cant_producto(product):
    cant_product = 0
    for i in range(0,8):
        if cupos[i][2] == product:
            cant_product += 1
    return cant_product
def peso_neto_total(product):
    neto_total = 0
    for i in range(0,8):
        if cupos[i][2] == product:
            neto_total +=cupos_numeros [i][2]
    return neto_total
def patente_mayor(product):
    mayor  = 0
    p_mayor = " "
    for i in range (0,8):
        if cupos[i][2] == product and cupos_numeros[i][2]> mayor:
            mayor = cupos_numeros[i][2]
            p_mayor = cupos[i][0]
    return p_mayor
def patente_menor(product):
    menor  = 45
    p_menor = " "
    for i in range (0,8):
        if cupos[i][2] == product and cupos_numeros[i][2]< menor:
            menor = cupos_numeros[i][2]
            p_menor = cupos[i][0]
    return p_menor
def limp_pantalla():
    if platform.system()== "Windows":
        os.system("cls")
    else:
        os.system("clear")

def mostrar_menup():
    global opcion_menu
    print ("ººº MENU PRINCIPALººº \n" )

    print ("1) ADMINISTRACIONES")
    print ("2) ENTREGA DE CUPOS ")
    print ("3) RECEPCION")
    print ("4) REGISTRAR CALIDAD")
    print ("5) REGISTRAR PESO BRUTO")
    print ("6) REGISTRAR DESCARGA")
    print ("7) REGISTRAR TARA")
    print ("8) REPORTES")
    print ("0) FIN DEL PROGRAMA")
    opcion_menu = input ("Elegir opcion: ")

def mostrar_menuadmi():
    print ("\nººº MENU ADMINISTRACIONES ººº\n")
    print ("a- TITULARES")
    print ("b- PRODUCTOS")
    print ("c- RUBROS")
    print ("d- RUBROS x PRODUCTO")
    print ("e- SILOS")
    print ("f- SUCURSALES")
    print ("g- PRODUCTO POR TITULAR")
    print ("v- VOLVER al MENU PRINCIPAL")

def mostrar_menuopciones():
    print ("\nººº MENU DE OPCIONES ººº\n")
    print ("a- ALTA")
    print ("b- BAJA")
    print ("c- CONSULTA")
    print ("m- MODIFICACION")
    print ("v- VOLVER AL MENÚ ANTERIOR")

def menu_b():
    global cant
    global p
    global proddis
    global producto
    mostrar_menuopciones()
    opcion_opcion =input("Elegir opcion: ")
    while opcion_opcion != "v": 
        limp_pantalla()
        if opcion_opcion == "a":
            mostrar_lista(proddis,5)
            print("[ 5 ] Terminar seleccion")
            p =int(input("Ingrese numero de producto que desea registrar / 5 para terminar: "))
            while p<0 or p > 5:
                print("Ingresaste un numero incorrecto,intenta denuevo...")
                p =int(input("Ingrese numero de producto que desea registrar / 5 para terminar: "))
            limp_pantalla()
            while p != 5 and cant < 3:
             mostrar_lista(proddis,5)
             print("[ 5 ] Terminar seleccion")
             producto [cant] = proddis[p]
             cant += 1
             if cant != 3:
                p =int(input("Ingrese numero de producto que desea registrar / 5 para terminar: "))
                while p <0 or p > 5 or buscar_lista(producto,3,proddis[p]):
                    if buscar_lista(producto,3,proddis[p]):
                        print("Este producto ya se registro...")
                    else:
                        print("Ingresaste un producto equivocado...")
                    p =int(input("Ingrese numero de producto que desea registrar / 5 para terminar: "))
             limp_pantalla()
             
             
            if cant == 3:
                print("Ya ingresaste los tres productos, ingrese a otro menu para modificarlos")
                input("Presione cualquier tecla para volver")
            limp_pantalla()

        if opcion_opcion == "b":
            mostrar_lista(producto,3)
            limp= int(input("Ingrese nº producto que desea eliminar: "))
            while limp >2 or limp <0  :
                print("Ingresaste un numero incorrecto,intenta denuevo...")
                limp= int(input("Ingrese producto que desea eliminar: "))
            producto [limp] = " "
            limp_pantalla()


        if opcion_opcion == "c":
            print( "listado de productos: ")
            mostrar_lista(producto,3)
            input("Presione cualquier tecla para volver")
            limp_pantalla()

        if opcion_opcion == "m":
            mostrar_lista(producto,3)

            cl= int(input("Ingrese nº producto que desea modificar: "))
            while cl >2 or cl <0  :
             cl= int(input("Ingrese nº producto que desea modificar: "))
            
            mostrar_lista(proddis,5)

            newp = int(input("Ingrese nº del nuevo producto: "))
            while newp <0 or newp>4 :
                newp = int(input("Ingrese nº del nuevo producto: "))
            producto[cl] = proddis[newp]
            limp_pantalla()
            
            
        if opcion_opcion != "a" and opcion_opcion != "b" and opcion_opcion != "c" and opcion_opcion != "m" and opcion_opcion != "v":

            print ("\nIngresaste una opcion inexistente, intenta denuevo...")
    
        mostrar_menuopciones()
        opcion_opcion =input("introduzca otra opcion: ")
        limp_pantalla()

def menu_admi():
    mostrar_menuadmi() 
    opcion_admi = input ("Elegir opcion: ")
    limp_pantalla()
    while opcion_admi != "v" : 
        
        if opcion_admi == "a" or (opcion_admi > "b" and opcion_admi <= "g"): # utilizamos codigo ascii para la comparacion

            menu_op()
        elif opcion_admi == "b" and pos >= 0:
            print("Ya no se pueden modificar los productos.")
            input("Presione cualquier tecla para continuar...")
        elif opcion_admi == "b" :
            menu_b()
  
        elif opcion_admi != "v":
            print("\nIngresaste una opcion inexistente, intenta denuevo...")

        mostrar_menuadmi()
        opcion_admi = input ("Elegir opcion: ")
        limp_pantalla()
      
def menu_op():
    mostrar_menuopciones()
    opcion_opcion =input("Elegir opcion: ")
    limp_pantalla()
    while opcion_opcion != "v": 
        
        if opcion_opcion == "a" or opcion_opcion == "b" or opcion_opcion == "c" or opcion_opcion == "m":

            print("\nEsta funcionalidad está en construcción... ")

        elif opcion_opcion != "v" :

            print ("\nIngresaste una opcion inexistente, intenta denuevo...")
    
        mostrar_menuopciones()
        opcion_opcion =input("introduzca otra opcion: ")
        limp_pantalla()

def entrega_de_cupos():
    global cupos
    global pos

    
    patente = input("ingresar patente del camion / 0 para salir: ").lower()
    while patente != "0" and not es_patente(patente):
        print("ingresaste una patente icorrecta, intenta denuevo...")
        patente = input("ingresar patente del camion / 0 para salir: ")
    

    while pos <7 and patente != "0" and not buscar_encupos(patente,0):

        pos = pos + 1
        
        cupos[pos][0] = patente
        cupos[pos][1] = "p"

        if pos != 7:
            patente = input("ingresar patente del camion / 0 para salir: ").lower()
            while patente != "0" and not es_patente(patente):
                print("ingresaste una patente icorrecta, intenta denuevo...")
                patente = input("ingresar patente del camion / 0 para salir: ")
    
    if buscar_encupos(patente,0) and pos!=7 :
        print("La patente ingrsada ya se registro con anterioridad...")
        input("Presione cualquier tecla para volver...")
       

def menu_3():
    global cant_camio
    global cupos

    patente = input("ingresar patente del camion / 0 para salir: ").lower()
    while patente != "0" and not es_patente(patente) :
        print("ingresaste una patente icorrecta, intenta denuevo...")
        patente = input("ingresar patente del camion / 0 para salir: ")

    while patente!= "0" and cant_camio <=8 and estado_camion(patente) == "p" and buscar_encupos(patente,0):

        mostrar_lista(producto,3)
        n_producto =int(input("Ingresar n° correspondiente al producto del camion: "))
        while n_producto <0 or n_producto >2:
            n_producto =int(input("Ingresar n° correspondiente al producto del camion: "))

        cant_camio +=  1
        cupos[buscar_posicion(cupos,8, patente)][1] = "e" 
        cupos[buscar_posicion(cupos,8, patente)][2] = producto [n_producto]

        if cant_camio != 8:
            patente = input("ingresar patente del camion / 0 para salir: ").lower()
            while patente != "0" and not es_patente(patente) :
                print("ingresaste una patente icorrecta, intenta denuevo...")
                patente = input("ingresar patente del camion / 0 para salir: ")

    if estado_camion(patente) != "p" and buscar_encupos(patente,0) :
        print("El camion no esta en estado pendiete... ")
        input("Presione cualquier tecla para volver")
    elif patente != "0" and not buscar_encupos(patente,0):
        print("La patente ingresada no esta registrada")
        input("Presione cualquier tecla para volver")


def menu_5():
    global cupos
    global cupos_numeros

    
    patente = input("ingresar patente del camion / 0 para salir: ").lower()
    while patente != "0" and not es_patente(patente) :
        print("ingresaste una patente icorrecta, intenta denuevo...")
        patente = input("ingresar patente del camion / 0 para salir: ")
    
    while patente!= "0" and buscar_encupos(patente,0) and estado_camion(patente) == "e" and cupos_numeros[buscar_posicion(cupos,8, patente)][0] == 0:
        

        peso_bruto = int(input("Ingresar peso bruto del camion(en toneladas): "))
        while peso_bruto < 1 or peso_bruto > 44:
            print("Ingresaste un peso bruto erroneo...")
            peso_bruto = int(input("Ingresar peso bruto del camion(en toneladas): "))

        cupos_numeros[buscar_posicion(cupos,8, patente)][0] = peso_bruto

        patente = input("ingresar patente del camion / 0 para salir: ").lower()
        while patente != "0" and not es_patente(patente) :
            print("ingresaste una patente icorrecta, intenta denuevo...")
            patente = input("ingresar patente del camion / 0 para salir: ")
    
    if patente != "0" and not buscar_encupos(patente,0)  :
        print("La patente ingresada no esta registrada...")
        input("Presione cualquier tecla para volver")
    elif patente != "0" and estado_camion(patente) != "e" and buscar_encupos(patente,0):
        print("Este camion no esta en estado pendiente...")
        input("Presione cualquier tecla para volver")
    elif patente != "0" and cupos_numeros[buscar_posicion(cupos,8, patente)][0] != 0:
        print("El camion ya registro su peso bruto...")
        input("Presione cualquier tecla para volver")
    limp_pantalla()
    

def menu_7():
    global cant_camio
    global cupos
    global cupos_numeros
    
    patente = input("ingresar patente del camion / 0 para salir: ").lower()
    while patente != "0" and not es_patente(patente) :
        print("ingresaste una patente icorrecta, intenta denuevo...")
        patente = input("ingresar patente del camion / 0 para salir: ").lower()

    while patente!= "0" and buscar_encupos(patente,0) and estado_camion(patente) == "e" and cupos_numeros[buscar_posicion(cupos,8, patente)][0] != 0 and cupos_numeros[buscar_posicion(cupos,8, patente)][1] == 0:

        tara = int(input("Ingresar tara del camion del camion: "))
        while tara >= cupos_numeros[buscar_posicion(cupos,8, patente)][0] or tara <1:
            print("Ingresaste una tara errona...")
            tara = int(input("Ingresar tara del camion del camion: "))

        cupos_numeros[buscar_posicion(cupos,8, patente)][1]  = tara
        cupos_numeros[buscar_posicion(cupos,8, patente)][2] = cupos_numeros[buscar_posicion(cupos,8, patente)][0] - tara
        patente = input("ingresar patente del camion / 0 para salir: ").lower()
        while patente != "0" and not es_patente(patente) :
            print("ingresaste una patente icorrecta, intenta denuevo...")
            patente = input("ingresar patente del camion / 0 para salir: ")


    if patente != "0" and not buscar_encupos(patente,0):
        print("La patente ingresada no esta registrada...")
        input("Presione cualquier tecla para volver")
    elif patente != "0" and estado_camion(patente) != "e" and buscar_encupos(patente,0):
        print("Este camion no esta en estado pendiente...")
        input("Presione cualquier tecla para volver")
    elif patente != "0" and cupos_numeros[buscar_posicion(cupos,8, patente)][0] == 0:
        print("El camion ingresado rodavia no registro el peso bruto...")
        input("Presione cualquier tecla para volver")
    elif patente != "0" and cupos_numeros[buscar_posicion(cupos,8, patente)][1] != 0:
        print("El camion ya registro su tara...")
        input("Presione cualquier tecla para volver")
    limp_pantalla()
        


def mostrar_report():
    global pos
    global cant_camio
    
    print("Cantidad de cupos otorgados: ", (pos + 1))
    print("Cantidad total de camiones recibidos: ", cant_camio)
    for i in proddis:
        if cant_producto(i) != 0:
            print("Cantidad total de camiones de ",i, ": ",cant_producto(i))
    for i in proddis:
        if cant_producto(i) != 0:
            print("Peso neto total de ",i, ": ",peso_neto_total(i))
    for i in proddis:
        if cant_producto(i) != 0:
            print ("Promedio del peso neto camión de ",i, ": ",(peso_neto_total(i) / cant_producto(i)))
    for i in proddis:
        if cant_producto(i) != 0:
            print("Patente del camión que mayor cantidad de ",i," descargó: ", patente_mayor(i))
    for i in proddis:
        if cant_producto(i) != 0:
            print("Patente del camión que menor cantidad de ",i," descargó: ", patente_menor(i))
        

mostrar_menup()
limp_pantalla()
while opcion_menu != "0" :
    
    
    if opcion_menu == "1": 
        menu_admi()
        limp_pantalla()
        
    elif opcion_menu == "2":
        if pos == 7:
            print("Ya estan todos los cupos ocupados...")
            input("Precione cualquier tecla para volver")
            limp_pantalla()
        else:
            entrega_de_cupos()
            limp_pantalla()

    elif opcion_menu == "3":
        if producto [0] == " " and producto[1] == " " and producto[2] == " ":
            print ("Primero debes seleccionar los productos disponibles ( menu administracion/productos )...")
            input("Presione cualquier tecla para volver")
        elif cant_camio == 8:
            print("Ya se registraron todos los camiones...")
            input("Presione cualquier tecla para volver")
        elif pos == -1:
            print("Todavia no hay camiones con cupos...")
            input("Presione cualquier tecla para volver")
        else:
            menu_3()
        limp_pantalla()

    elif opcion_menu == "5":
        if cant_camio == 0:
            print("Todavia no hay camiones que pasaron por recepcion...")
            input("Presione cualquier tecla para volver")
        else:
            menu_5()

    elif opcion_menu == "7":
        if cant_camio == 0:
            print("Todavia no hay camiones que pasaron por recepcion...")
            input("Presione cualquier tecla para volver")
        else:
            menu_7()
            
    elif opcion_menu =="4" or opcion_menu =="6":
        print ( "\nEsta funcionalidad está en construcción... introduzca otra opcion")
        input("Presione cualquier tecla para volver")
        
    elif opcion_menu == "8"  :
        if pos != -1:
            mostrar_report()
            input ("\ningrese cualquier caracter para volver al menu principal....") 
        else:
            print("Todavia no se registro ningun camion...")
            input("Presione cualquier tecla para volver")
        
    elif opcion_menu != "0":
        print("\nIngresaste una opcion inexistente, intenta denuevo...") 

    mostrar_menup()
    limp_pantalla()
     

    