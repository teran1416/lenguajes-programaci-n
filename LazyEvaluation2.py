#generador perezoso de multiplos de m, genera uno a la vez: yield lo retorna y espera a que le pidan el siguiente
def multM(m):
    num = 0
    while True:
        if num % m ==0:
            yield num
        num = num +1



generadorMultiplos = multM(7)

print(next(generadorMultiplos))
print(next(generadorMultiplos))
print(next(generadorMultiplos))

#

try:
    pass

except StopIteration:
    print("se ha producido un error consumiendo datos del generador")