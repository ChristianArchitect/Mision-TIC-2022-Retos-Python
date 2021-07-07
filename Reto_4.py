# Enunciado
# Reto 4: Detectando monedas repetidas
'''
Se cuenta con una máquina capaz de detectar monedas de la misma denominación, es decir del mismo valor repetido, en un conjunto de estas monedas. A la máquina se introducen las monedas una por una y esta contaría el número de monedas repetidas. El inconveniente con esta máquina es que existen diferentes modelos y estos se diferencian básicamente solo en el tamaño de su memoria digital, es decir cuantas monedas puede recordar a medida que se van introduciendo. Por ejemplo, una máquina con una memoria de tamaño 3 solo podría comparar la nueva moneda introducida con las 3 últimas monedas introducidas a la máquina y con eso contar las repeticiones. Una máquina con un tamaño de memoria 1 solo podría comparar a la moneda actual con la anterior moneda introducida.

Lamentablemente el tamaño de la memoria no se reconoce de forma automática dentro de la máquina, sino que se debe ingresar de forma manual por las personas encargadas de introducir las monedas cada vez.

Para verificar cuantas monedas repetidas se dejan de contar de acuerdo al tamaño de las memorias de las máquinas y justificar una actualización de estas, se ha decidido solicitar su ayuda para construir un programa en Python que permita verificar la calidad, comprobando cuántas monedas repetidas se están contando en la máquina en función del tamaño de su memoria y el número real de monedas repetidas.
'''
# ENTRADA
'''
La entrada estará formada por dos líneas:
La primera línea aparecerán dos números N y K que indican el número de monedas a verificar y el tamaño de la memoria de la máquina (1≤N≤10000,1≤K≤1000).
La segunda línea contiene N números (entre 1 y 100) separados por espacios que representan las monedas introducidas en la máquina.
Dos monedas se consideran iguales si están representadas por el mismo número.
'''
# SALIDA
'''
El programa imprimirá dos números separados por un espacio.

El primero representará el número real de monedas repetidas.
El segundo representará la cantidad de monedas repetidas detectadas por la máquina en función de su memoria considerando que esta solo es capaz de guardar en memoria las K monedas anteriores.
'''

# DESARROLLO DEL EJERCICIO
# INPUT cantidad de monedas a evaluar, rango para evaluar esas monedas
valor_n, valor_k = input().split()
# convertir los valores N y K a enteros
valor_n = int(valor_n)
valor_k = int(valor_k)
# INPUT entrada de la lista de monedas a evaluar
lista_entrada = input().split()
# inicia con una lista vacia ListaMonedas
listaMonedas = []
# recorre los valores introducidos en la cadena lista_entrada
for moneda in lista_entrada:
    # la moneda es diferente a una cadena vacia
    if moneda != ' ':
        # convierte el valor str a int
        m = int(moneda)
        # agrega el valor convertido en int a la lista vacia ListaMonedas
        listaMonedas.append(m)
    # ENDIF
# ENDFOR  al final de esta lista todas las monedas estaran convertidas y agregadas
# !!! Hasta este punto el codigo funciona perfectamente !!! #

listaMonedas2 = listaMonedas[:]  # copio toda la lista en una segunda lista
cantRepetidas = 0
contador = 0
while contador < valor_n:
    myCoin = listaMonedas[0]
    del listaMonedas[0]
    if myCoin in listaMonedas:
        cantRepetidas += 1
    contador += 1
# !!! Hasta este punto el codigo funcion perfectamente !!! #

memoria = 0
index = 0
for valor in listaMonedas2:
    myValue = valor
    magic = index + valor_k
    if magic < valor_n:
        index += 1
        if myValue in listaMonedas2[index:magic+1]:
            memoria += 1


print(f'{cantRepetidas} {memoria}')
#  el ejercicio funciona perfectamente, Felicitaciones!!!
