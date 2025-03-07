from functools import reduce

#lector de datos de un csv que funciona como un generador para un evaluador perezoso:
def loadData(filePath):
    with open(filePath,mode="r",encoding="utf-8") as file:
        headers = file.readline().strip().split(",") #leer encabezado como las claves del diccionario
        for line in file:
            values = line.strip().split(",")
            record = dict(zip(headers, values))
            yield record

def USD_to_COP(x):
    pass
def filter7Mill():
    pass
def SumAll():
    pass

dataStream = loadData("dataset.csv")

#consumir tres registros y mostrarlos por pantalla:
datalocal = []
datalocal.append(next(dataStream))
datalocal.append(next(dataStream))
datalocal.append(next(dataStream))

print(datalocal)

#Convertir campo "salario de USD to COP mapeando una funcion de conversion de divisas:"
#{'ID': '1' 'Nombre': 'Ana' ''}
listaSalarioPesos= list(map(USD_to_COP,datalocal))

#Filtrar aquellos que tengan un salario mayor a $Cop 7`000.000
listaMayores = list(filter(filter7Mill, listaSalarioPesos))

#Sumar el total de salarios de esas personas con reduce:
sumaTotal = reduce(SumAll, listaMayores)

