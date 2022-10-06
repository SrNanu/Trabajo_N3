
import opcode
from operator import truediv
from string import ascii_letters
import platform
import os
import os.path
import pickle
import io


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
producto = [" "] *3 
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

class productos:
    def __init__(self) :
        self.nombre= " "
        self.codigo= 0
        self.habilitado = "T"
class rubros:
    def __init__(self) :
        self.nombre = " "
        self.codigo = 0
class rubrosxproductos:
    def __init__(self):
        self.codi_p= 0
        self.codi_r= 0
        self.minimo = 0.00
        self.maximo = 0.00
class silos:
    def __init__(self) :
        self.codigo = 0
        self.nombre = ""
        self.codi_p = 0
        self.stock = 0
    


p = productos()
r = rubros()
rxp = rubrosxproductos()
s= silos()
p_largo = 105
r_largo = 86
rxp_largo = 114
s_largo = 109
productos_fisico = "C:\\Users\\Cataldi\\Desktop\\Santino\\Facultad\\Algoritmo y Estructura de Datos\\Trabajo_n3\\productos.bat"
rubros_fisico = "C:\\Users\\Cataldi\\Desktop\\Santino\\Facultad\\Algoritmo y Estructura de Datos\\Trabajo_n3\\rubros.bat"
rubrosxproductos_fisico = "C:\\Users\\Cataldi\\Desktop\\Santino\\Facultad\\Algoritmo y Estructura de Datos\\Trabajo_n3\\rubrosxproductos.bat"
silos_fisico ="C:\\Users\\Cataldi\\Desktop\\Santino\\Facultad\\Algoritmo y Estructura de Datos\\Trabajo_n3\\silos.bat"
    
#Funciones



        
def mostrar_productos():
    a = productos()
    if os.path.exists(productos_fisico):
        productos_logico= open(productos_fisico,"r+b")
    else:
        productos_logico = open(productos_fisico,"w+b")

    t = os.path.getsize(productos_fisico)
    productos_logico.seek(0)
    while productos_logico.tell()< t:
        a = pickle.load(productos_logico)
        if a.habilitado == "T" :
            print("---------------------------------")
            print("Nombre: ", a.nombre)
            print("Codigo: ", a.codigo)
            print("habilitado: ", a.habilitado)
    productos_logico.close()
            
def buscar_rubro(rub):
    t = os.path.getsize(rubros_fisico)
    if os.path.exists(rubros_fisico):
        rubros_logico= open(rubros_fisico,"r+b")
    else:
        rubros_logico = open(rubros_fisico,"w+b")

    rubros_logico.seek(0)
    while rubros_logico.tell()< t:
        pos =  rubros_logico.tell()
        a = pickle.load(rubros_logico)
        if a.nombre == rub:
            return pos
    return -1
def buscar_producto(prod):
    t = os.path.getsize(productos_fisico)
    if os.path.exists(productos_fisico):
        productos_logico= open(productos_fisico,"r+b")
    else:
        productos_logico = open(productos_fisico,"w+b")

    productos_logico.seek(0)
    while productos_logico.tell()< t:
        pos =  productos_logico.tell()
        a = pickle.load(productos_logico)
        if a.nombre == prod:
            return pos
    return -1
    
    
def buscar_codigo(c):
    t = os.path.getsize(productos_fisico)
    if os.path.exists(productos_fisico):
        productos_logico= open(productos_fisico,"r+b")
    else:
        productos_logico = open(productos_fisico,"w+b")

    productos_logico.seek(0)
    while productos_logico.tell()< t:
        pos =  productos_logico.tell()
        a = pickle.load(productos_logico)
        if a.codigo == c:
            return pos
    return -1
    productos_logico.close()
def buscar_codirubro(c):
    t = os.path.getsize(rubrosxproductos_fisico)
    if os.path.exists(rubrosxproductos_fisico):
        rubrosxproductos_logico= open(rubrosxproductos_fisico,"r+b")
    else:
        rubrosxproductos_logico = open(rubrosxproductos_fisico,"w+b")

    rubrosxproductos_logico.seek(0)
    while rubrosxproductos_logico.tell()< t:
        pos =  rubrosxproductos_logico.tell()
        a = pickle.load(rubrosxproductos_logico)
        if a.codigo == c:
            return pos
    return -1
    rubrosxproductos_logico.close()
def buscar_silo(sil):
    t = os.path.getsize(silos_fisico)
    if os.path.exists(silos_fisico):
        silos_logico= open(silos_fisico,"r+b")
    else:
        silos_logico = open(silos_fisico,"w+b")

    silos_logico.seek(0)
    while silos_logico.tell()< t:
        pos =  silos_logico.tell()
        a = pickle.load(silos_logico)
        if a.nombre == sil:
            return pos
    return -1

        
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
            if os.path.exists(productos_fisico):
                productos_logico= open(productos_fisico,"r+b")
            else:
                productos_logico = open(productos_fisico,"w+b")

        
            p.nombre = input("Ing nombre de nuevo producto ( menor a 20 caracteres): ")
            p.nombre = p.nombre.ljust(20) 
            
            while len(p.nombre) > 20 or buscar_producto(p.nombre) != -1:
                if buscar_producto(p.nombre) !=-1:
                    print("ingresaste un producto que ya existe.")
                else:
                    print("Ingresaste un nombre incorrecto,intenta denuevo.")
                p.nombre = input("Ing nombre de nuevo producto ( menor a 20 caracteres): ")
                p.nombre = p.nombre.ljust(20)
            while p.nombre != "0                   ":
             
             p.codigo = int(os.path.getsize(productos_fisico) / p_largo) 
             
             productos_logico.seek(os.path.getsize(productos_fisico))
             pickle.dump(p, productos_logico)
             productos_logico.flush()
             
             p.nombre = input("Ing nombre de nuevo producto ( menor a 20 caracteres): ")
             p.nombre = p.nombre.ljust(20) 
             while len(p.nombre) > 20 or buscar_producto(p.nombre) != -1:
                if buscar_producto(p.nombre) !=-1:
                    print("ingresaste un producto que ya existe.")
                else:
                    print("Ingresaste un nombre incorrecto,intenta denuevo.")
                p.nombre = input("Ing nombre de nuevo producto ( menor a 20 caracteres): ")
            productos_logico.close()
             
             
        
            
    
        if opcion_opcion == "b":
            if os.path.exists(productos_fisico):
                productos_logico= open(productos_fisico,"r+b")
            else:
                productos_logico = open(productos_fisico,"w+b")
            mostrar_productos()
            limp= int(input("Ingrese codigo producto que desea eliminar: "))
            while buscar_codigo(limp) ==-1:
                print("Ingresaste un numero incorrecto,intenta denuevo...")
                limp= int(input("Ingrese producto que desea eliminar: "))
            productos_logico.seek(buscar_codigo(limp)) 
            n = pickle.load(productos_logico)
            n.habilitado = "F"
            productos_logico.seek(buscar_codigo(limp)) 
            pickle.dump(n, productos_logico)
            productos_logico.flush()
            productos_logico.close()
            limp_pantalla()


        if opcion_opcion == "c":
            print( "Listado de productos: ")
            mostrar_productos()
            input("Presione cualquier tecla para volver")
            limp_pantalla()

        if opcion_opcion == "m":
            if os.path.exists(productos_fisico):
                productos_logico= open(productos_fisico,"r+b")
            else:
                productos_logico = open(productos_fisico,"w+b")
            mostrar_productos()

            print("***SOLO PUEDE MODIFICAR EL NOMBRE DEL PRODUCTO***")
            cl= int(input("Ingrese codigo producto que desea modificar: "))
            
            while buscar_codigo(cl) == -1: 
             print("Ingresaste codigo incorrecto, intenta denuevo...")
             cl= int(input("Ingrese nº producto que desea modificar: "))
             
            productos_logico.seek(cl * p_largo)
            p =pickle.load(productos_logico)
            newp = input("Ingrese nuevo nombre del producto: ")
            
            while buscar_producto(newp) != -1: 
                print("Ingresaste un producto ya existente, intenta denuevo...")
                newp = input("Ingrese nuevo nombre del producto: ")
            p.nombre = newp
            p.nombre = p.nombre.ljust(20)
            productos_logico.seek(cl * p_largo)
            pickle.dump(p,productos_logico)
            productos_logico.flush()
            productos_logico.close()
            limp_pantalla()
            
            
        if opcion_opcion != "a" and opcion_opcion != "b" and opcion_opcion != "c" and opcion_opcion != "m" and opcion_opcion != "v":

            print ("\nIngresaste una opcion inexistente, intenta denuevo...")
    
        mostrar_menuopciones()
        opcion_opcion =input("introduzca otra opcion: ")
        limp_pantalla()
def menu_c():
    mostrar_menuopciones()
    opcion_c = input ( "Ingrese opcion: ")
    limp_pantalla()
    while opcion_c != "v":
        if opcion_c == "a":
            if os.path.exists(rubros_fisico):
                rubros_logico= open(rubros_fisico,"r+b")
            else:
                rubros_logico = open(rubros_fisico,"w+b")

        
            r.nombre = input("Ing nombre de nuevo rubro ( menor a 20 caracteres): ")
            r.nombre = r.nombre.ljust(20) 
            
            while len(r.nombre) > 20 or buscar_rubro(r.nombre) != -1:
                if buscar_rubro(r.nombre) !=-1:
                    print("ingresaste un rubro que ya existe.")
                else:
                    print("Ingresaste un nombre incorrecto,intenta denuevo.")
                r.nombre = input("Ing nombre de nuevo rubro ( menor a 20 caracteres): ")
                r.nombre = r.nombre.ljust(20) 
            while r.nombre != "0                   ":
             
             r.codigo = int(os.path.getsize(rubros_fisico) / r_largo) 
             
             rubros_logico.seek(os.path.getsize(rubros_fisico))
             pickle.dump(r, rubros_logico)
             rubros_logico.flush()
             
             r.nombre = input("Ing nombre de nuevo producto ( menor a 20 caracteres): ")
             r.nombre = r.nombre.ljust(20) 
             while len(r.nombre) > 20 or buscar_rubro(r.nombre) != -1:
                if buscar_rubro(r.nombre) !=-1:
                    print("ingresaste un producto que ya existe.")
                else:
                    print("Ingresaste un nombre incorrecto,intenta denuevo.")
                r.nombre = input("Ing nombre de nuevo producto ( menor a 20 caracteres): ")
            rubros_logico.close()
        if opcion_c == "b" or opcion_c == "c" or opcion_c == "m":
            print ("Esta funcionalidad esta en construccion...")
            input("Presione cualquier tecla para volver ")
            limp_pantalla()
        if opcion_c != "a" and opcion_c != "b" and opcion_c != "c" and opcion_c != "m" and opcion_c != "v":
            print("Ingresaste una opcion inexistente, intenta denuevo...")
        mostrar_menuopciones()
        opcion_c = input ( "Ingrese opcion: ")
        limp_pantalla()
def menu_d():
    mostrar_menuopciones()
    opcion_d = input ( "Ingrese opcion: ")
    limp_pantalla()
    while opcion_d != "v":
        if opcion_d == "a":
            
            if os.path.exists(rubrosxproductos_fisico):
                rubrosxproductos_logico= open(rubrosxproductos_fisico,"r+b")
            else:
                rubrosxproductos_logico = open(rubrosxproductos_fisico,"w+b")

        
            rxp.codi_p = int(input("Ing codigo de producto: "))
            while  buscar_codigo(rxp.codi_p) == -1:
                print("ingresaste un producto que no existe.")
                
                rxp.codi_p = int(input("Ing codigo de producto: "))
            rxp.codi_r = int (input("Ing codigo de rubro"))
            while buscar_codirubro(rxp.codi_r)== -1:
                print("ingresaste un rubro que no existe.")
                rxp.codi_r = int (input("Ing codigo de rubro"))
            rxp.minimo = float("Ingresar valor minimo admitido(entre 0 y 100)")
            while rxp.minimo > 100 or rxp.minimo < 0:
                print("ingresaste un  valor equivocado.")
                rxp.minimo = float("Ingresar valor minimo admitido(entre 0 y 100)")
            rxp.maximo = float("Ingresar valor maximo admitido(entre 0 y 100)")
            while rxp.maximo > 100 or rxp.maximo < 0:
                print("ingresaste un  valor equivocado.")
                rxp.maximo = float("Ingresar valor maximo admitido(entre 0 y 100)")
                
            rubrosxproductos_logico.seek(os.path.getsize(rubrosxproductos_fisico))
            pickle.dump(rxp,rubrosxproductos_logico)
            rubrosxproductos_logico.flush()
            rubrosxproductos_logico.close()
        if opcion_d == "b" or opcion_d == "c" or opcion_d == "m":
            print ("Esta funcionalidad esta en construccion...")
            input("Presione cualquier tecla para volver ")
            limp_pantalla()
        if opcion_d != "a" and opcion_d != "b" and opcion_d != "c" and opcion_d != "m" and opcion_d != "v":
            print("Ingresaste una opcion inexistente, intenta denuevo...")
        mostrar_menuopciones()
        opcion_d = input ( "Ingrese opcion: ")
        limp_pantalla()
        
def menu_e():
    mostrar_menuopciones()
    opcion_e = input ( "Ingrese opcion: ")
    limp_pantalla()
    while opcion_e != "v":
        if opcion_e == "a":
            if os.path.exists(silos_fisico):
                silos_logico= open(silos_fisico,"r+b")
            else:
                silos_logico = open(silos_fisico,"w+b")
        s.nombre = input("Ingrese nombre del silo (menor a 20 caracteres): ") #podria verificarse la longitud
        s.nombre = s.nombre.ljust(20)
        while buscar_silo() != -1 :
            print("Ingresaste un silo que ya existe.")
            s.nombre = input("Ingrese nombre del silo (menor a 20 caracteres): ") 
            s.nombre = s.nombre.ljust(20)
        s.codigo = int(os.path.getsize(silos_fisico)/ s_largo)
        s.codi_p = int(input("Ing codigo de producto: "))
        while  buscar_codigo(s.codi_p) == -1:
            print("ingresaste un producto que no existe.")
            
            s.codi_p = int(input("Ing codigo de producto: "))
        silos_logico.seek(os.path.getsize(silos_fisico))
        pickle.dump(s,silos_logico)
        silos_logico.flush()
        silos_logico.close
        if opcion_e == "b" or opcion_e == "c" or opcion_e == "m":
            print ("Esta funcionalidad esta en construccion...")
            input("Presione cualquier tecla para volver ")
            limp_pantalla()
        if opcion_e != "a" and opcion_e != "b" and opcion_e != "c" and opcion_e != "m" and opcion_e != "v":
            print("Ingresaste una opcion inexistente, intenta denuevo...")
        mostrar_menuopciones()
        opcion_e = input ( "Ingrese opcion: ")
        limp_pantalla()
#falta verificar     
            
            
    

def menu_admi():
    mostrar_menuadmi() 
    opcion_admi = input ("Elegir opcion: ")
    limp_pantalla()
    while opcion_admi != "v" : 
        
        if opcion_admi == "a" or opcion_admi == "f" or opcion_admi == "g": 

            menu_op()
        elif opcion_admi == "b" :
            menu_b()
        elif opcion_admi == "c":
            menu_c()
        elif opcion_admi == "d":
            menu_d()
        elif opcion_admi == "e":
            menu_e()
  
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
     

    