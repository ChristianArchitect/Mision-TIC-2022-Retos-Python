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

# start
numero_N, numero_K = input().split()
numero_N = int(numero_N)
numero_K = int(numero_K)

listaMonedas = input().split()
repReal = 0
repDetectadas = 0
indice = 0
for moneda in listaMonedas:
    if moneda == listaMonedas[numero_K]
