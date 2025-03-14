import functools

#para cargar datos
def cargar_datos_csv(ruta):
    with open(ruta, 'r') as archivo:
       
        encabezado = archivo.readline().strip().split(',')
        
        # Leemos cada línea del archivo para el diccionario
        for linea in archivo:
            valores = linea.strip().split(',')
            yield dict(zip(encabezado, valores))

# 2. filtrar personajes con nivel mayor a 10
def filtrar_nivel(personaje):
    return int(personaje['nivel']) > 10

# 3.para agregar el campo 'totalPower' a cada personaje
def calcular_total_power(personaje):
    ataque = int(personaje['ataque'])
    defensa = int(personaje['defensa'])
    personaje['totalPower'] = ataque + defensa
    return personaje

# 4.para encontrar el personaje con el mayor poder
def mayor_poder(personaje1, personaje2):
    if personaje1['totalPower'] > personaje2['totalPower']:
        return personaje1
    return personaje2

# 5. Main para realizar el análisis
def analizar_personajes(ruta_csv):
    # Cargar los datos
    personajes = cargar_datos_csv(ruta_csv)
    
    # Filtrar personajes con nivel > 10
    personajes_filtrados = list(filter(filtrar_nivel, personajes))
    
    # Imprimir nivel mayor a 10
    print("Personajes con nivel mayor a 10:")
    for personaje in personajes_filtrados:
        print(f"- {personaje['nombre']} (Nivel: {personaje['nivel']})")
    
    
    # Crear la lista con el campo 'totalPower'
    personajes_con_power = map(calcular_total_power, personajes_filtrados)
    
    # Encontrar el personaje con mayor poder total
    personaje_mayor_poder = functools.reduce(mayor_poder, personajes_con_power)
    
    return personaje_mayor_poder

# Llamamos a la función de análisis con el archivo 'personajes.csv'
personaje_con_mayor_poder = analizar_personajes('personajes.csv')

# Mostrar el resultado
print(f"\nEl personaje con mayor poder y que tene nivel mayor a 10 es:: {personaje_con_mayor_poder['nombre']}, sumando su ataque y defensa como decia el enunciado, con un total de {personaje_con_mayor_poder['totalPower']}")
