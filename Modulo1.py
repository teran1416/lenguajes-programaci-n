def cargarDatos(file):
    datos =[]
    with open(file, "r",encoding="utf-8") as buffer: #buffer de lectura
        for linea in buffer:
            linea= linea.strip() #eliminar espacios en blanco
            datos.append(linea)

    return datos
