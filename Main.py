from Modulo1 import*

nombre_archivo = input("ingrese nombre de el archivo: ")

lista_datos = cargarDatos(nombre_archivo)

for linea in  lista_datos:
 print ("\n" + linea)