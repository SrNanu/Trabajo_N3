import pickle
import os


productos_fisico = "C:\\Users\\Cataldi\\Desktop\\Santino\\Facultad\\Algoritmo y Estructura de Datos\\Trabajo_n3\\productos.bat"
productos_logico = open(productos_fisico,"w+b")
class productos:
    def __init__(self) :
        self.codigo = 0
        self.nombre = ""
        self.codi_p = 0
        self.stock = 0

p = productos()
p.nombre = input()
p.nombre = p.nombre.ljust(20)
print (p.nombre)
p.codigo = 2
 #114
pickle.dump(p, productos_logico)
productos_logico.flush()
print(os.path.getsize(productos_fisico))