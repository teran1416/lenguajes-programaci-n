from functools import reduce

# Lector de datos de un csv que funciona como un generador para un evaluador perezoso:
def loadData(filePath):
    with open(filePath, mode="r", encoding="utf-8") as file:
        headers = file.readline().strip().split(",")  # Leer encabezado como las claves del diccionario
        for line in file:
            values = line.strip().split(",")
            record = dict(zip(headers, values))
            yield record

# Convertir salario de USD a COP
def USD_to_COP(registro):
    registro["Salario"] = int(registro["Salario"]) * 4100  # Convertir el salario a COP
    return registro  


def filter7Mill():
    pass


def SumAll(x,y):
   pass

dataStream = loadData("dataset.csv")

# Consumir tres registros y mostrarlos por pantalla:
datalocal = []
#filtar el stream hasta que no haya nada más: 
try:
    for __ in range(1000):
        datalocal.append(next(dataStream))
except StopIteration:
    print("no hay más datos")


# datalocal.append(next(dataStream))
# datalocal.append(next(dataStream))
# datalocal.append(next(dataStream))

print(datalocal)

# Convertir el campo "Salario" de USD a COP mapeando una función de conversión de divisas:
listaSalarioPesos = list(map(USD_to_COP, datalocal))
print(listaSalarioPesos)

# Filtrar aquellos que tengan un salario mayor a 7,000,000 COP
listaMayores = list(filter(lambda e: int(e["Salario"]) > 7000000, listaSalarioPesos))
print("\nTodos los usarios con salarios mayores a cop 7.000.000")
print(listaMayores)

# Sumar el total de salarios de esas personas con reduce
print("\Suma del salario de esos empleados")
sumaTotal = reduce(lambda acum, e: acum + int(e["Salario"]), listaMayores, 0)

print(f"Todos ganan: {sumaTotal}")



