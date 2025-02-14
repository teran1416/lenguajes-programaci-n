# #Conceptos basicos de programacion funcional

# #1. Funciones son ciudadanos de primer orden

# # la definicion de uan funcion puede ser asignada a una variable con referencia 
# def suma (a,b):
#     return a+b

# def resta(a,b):
#     return a-b

# def multi(a,b):
#     return a*b

# def div(a,b):
#     if b != 0:
#         return a/b

# val1 = int(input("ingrese valor 1"))
# val2 = int(input("ingrese valor 2"))
# op = int(input("ingrese la operacion: 1. suma 2. resta 3.multi 4. div"))

# if op == 1:
#     operacion = suma
# elif op == 2:
#     operacion = resta
# elif op == 3:
#     operacion = multi
# elif op == 4:
#     operacion = div
# else:
#     print("Operacion no valida")
    
# print(f"el resultado es: {operacion(val1,val2)}")

# # x = suma
# # y= suma

# # print(x(5,3))
# # print(y(6,8))



# #Ejemplo: Una calculadora

# #2. Funciones puras
# #3. funciones anonimas(lambda)
# num = int(input("ingrese un numero cualquiera:"))
# es_par = lambda x: x % 2 == 0
# print(es_par(27))
# print(f"{num} es par?: {es_par(num)}")

#4. funciones de orden superior

# 4. a MAP
#ejemplo sin map: normalizar un conjunto de datos:
ciudades = ["Cali", "medellin", "BOGOTA", "bArrAnQuillA"]
 
 #es una funcion pura?
def normalizar_datos(lista_nombres):
    datos_norm = []
    for nombre in lista_nombres:
        datos_norm.append(nombre.capitalize())
    return datos_norm

#usando map, sin funcion lambda:
def capitalizar(palabra):
    #retorna la palabra con la inicial en mayuscula
    return palabra.capitalize()

ciudades_norm2 = list(map(capitalizar, ciudades))


ciudades_norm = normalizar_datos(ciudades)
print(f"datos sin normalizar:{ciudades}")
print(f"datos normalizados:{ciudades_norm}")
print(f"Datos normalizados con map (sin lambda):{ciudades_norm2}")


#ejemplo de una funcion de orden superior : map
ciudades_norm3 = list(map (lambda n: n.capitalize(), ciudades))
print(f"Datos normalizados con map (con lambda):{ciudades_norm3}")