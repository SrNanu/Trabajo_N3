import pickle
import os


productos_fisico = "C:\\Users\\Cataldi\\Desktop\\Santino\\Facultad\\Algoritmo y Estructura de Datos\\Trabajo_n3\\productos.bat"
productos_logico = open(productos_fisico,"w+b")
class productos:
    def __init__(self) :
        self.nombre= " "
        self.codigo= 0
        self.habilitado = "T"

p = productos()
p.nombre= "holsajajas"
p.nombre =p.nombre.ljust(20,"-")
p.codigo = 2
p.habilitado = "F"
print (p.nombre)
pickle.dump(p, productos_logico)
productos_logico.flush()
print(os.path.getsize(productos_fisico))