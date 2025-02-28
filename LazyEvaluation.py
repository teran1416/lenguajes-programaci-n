import random

def LazyRandomGenerator():
    while True:
        #la instruccion yiel devuelve el valor (es un return) pero espera el "next" del consumidor
        yield random.randint(1,1000)


GeneradorAleatorios = LazyRandomGenerator()

print(next(GeneradorAleatorios))
print(next(GeneradorAleatorios))
print(next(GeneradorAleatorios))
print(next(GeneradorAleatorios))
print(next(GeneradorAleatorios))


for _ in range(100):
#     #cuando se invoca el next del generador, el generador devuelve un valor y espera el siguiente next con yield
 print(next(GeneradorAleatorios))


    