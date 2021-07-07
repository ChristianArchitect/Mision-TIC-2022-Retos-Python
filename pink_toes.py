# numeros = input('escriba numeros: ').split()
# print(numeros)
# for numero in numeros:
#     print(numero)
#     print(type(numero))
#     numero = int(numero)
#     print(numero)
#     print(type(numero))

# start
# numero_N, numero_K = input().split()
# numero_N = int(numero_N)
# numero_K = int(numero_K)


# listaMonedas = input().split()
# for m in listaMonedas:
#     n = int(m)
#     listaMonedas.append(n)
#     listaMonedas.remove(m)
# print(listaMonedas)


# codigo util del ejercicio
# numero_n, numero_k = input().split()
# numero_n = int(numero_n)
# numero_k = int(numero_k)

# lista_entrada = input().split()
# listaMonedas = []
# for moneda in lista_entrada:
#     if moneda != ' ':
#         m = int(moneda)
#         listaMonedas.append(m)

# rangoMax = numero_k
# memoriaRep = 0
# for moneda in listaMonedas:
#     for index in range(moneda, rangoMax):
#         if moneda == index:
#             memoriaRep += 1

# numero_n, numero_k = input().split()
# numero_n = int(numero_n)
# numero_k = int(numero_k)

# lista_entrada = input().split()
# listaMonedas = []
# for moneda in lista_entrada:
#     if moneda != ' ':
#         m = int(moneda)
#         listaMonedas.append(m)

# listaRepetidos = []
# listaMonedas = [1, 2, 3, 1, 2, 3, 4, 5]
# for moneda1 in listaMonedas:
#     print(moneda1)
#     bandera = 0
#     for moneda2 in listaMonedas:
#         if moneda2 == moneda1:
#             if moneda1 not in listaRepetidos:
#                 bandera += 1
#                 if bandera == 2:
#                     listaRepetidos.append(moneda1)
#                     break
# print(listaRepetidos)

# listaMonedas = [1, 2, 3, 1, 2]
# maximo = 3
# encontrado = 0
# contador = 0
# iterador = 0
# for numero in listaMonedas:
#     nuevaLista = listaMonedas[numero-1:(numero+maximo)-1]
#     print(nuevaLista)
#     if numero in nuevaLista:
#         print(f'{numero} esta en la lista')

'''
listaRepetidas = []
for moneda1 in listaMonedas:
    # imprimo que moneda estoy evaluando para guiarme
    print(f'Moneda Evaluada: {moneda1}')
    cantRep = 0
    for moneda2 in listaMonedas:
        if moneda1 == moneda2:
            cantRep += 1
    print(cantRep)
    del listaMonedas[0]
    if cantRep > 1:
        listaRepetidas.append(moneda1)
'''


# def ElimaListaWhile(lista, longitud):
#     '''Esta funcion recorre una lista de una logitud determinada y elimina el primer elemento
#     de la lista actual hasta dejarla con un solo elemento'''
#     # lista = [1, 2, 3, 1, 2]
#     # longitud = 5
#     longWhile = longitud - 1
#     indice = 0
#     while indice <= longWhile:
#         print(lista)
#         del lista[0]
#         indice = indice + 1
#     # [1, 2, 3, 1, 2]
#     # [2, 3, 1, 2]
#     # [3, 1, 2]
#     # [1, 2]
#     # [2]


# def RecorreListaConFor(lista, rango):
#     '''Esta funcion recorre una lista de y teneindo en cuenta un rango,
#     busca un valor en ese fragmento de la lista'''
#     memoria = 0
#     rango = 2
#     lista = [5, 2, 3, 1, 2]
#     for valor in lista:
#         print(f'valor: {valor}')
#         if valor in lista[1:rango]:  # EUREKA!!
#             print('Esta')
#         else:
#             print('No esta')


# DESARROLLO DEL EJERCICIO
# INPUT cantidad de monedas a evaluar, rango para evaluar esas monedas
# valor_n, valor_k = input().split()
# convertir los valores N y K a enteros
# valor_n = int(valor_n)
# valor_k = int(valor_k)
# INPUT entrada de la lista de monedas a evaluar
# lista_entrada = input().split()
# inicia con una lista vacia ListaMonedas
# listaMonedas = []
# recorre los valores introducidos en la cadena lista_entrada
# for moneda in lista_entrada:
# la moneda es diferente a una cadena vacia
# if moneda != ' ':
# convierte el valor str a int
# m = int(moneda)
# agrega el valor convertido en int a la lista vacia ListaMonedas
# listaMonedas.append(m)
# ENDIF
# ENDFOR  al final de esta lista todas las monedas estaran convertidas y agregadas
# !!! Hasta este punto el codigo funciona perfectamente !!! #


# !!! Hasta este punto el codigo funcion perfectamente !!! #

# memoria = 0
# range = 2
# lista = [5, 2, 3, 1, 2]
# for valor in lista:
#     print(f'valor: {valor}')
#     myValue = valor
#     valorSum = valor + range
#     if myValue in lista[valor:]:
#         print('Esta')
#     else:
#         print('No esta')


# cantRepetidas = 0
# contador = 0
# while contador < valor_n:
#     myCoin = listaMonedas[0]
#     del listaMonedas[0]
#     if myCoin in listaMonedas:
#         cantRepetidas += 1
#     contador += 1
# print(cantRepetidas)
# !!! Hasta este punto el codigo funcion perfectamente !!! #

# memoria = 0
# rango = 2
# lista = [1, 2, 3, 1, 2]
# index = 0
# for valor in lista:
#     print(f'valor: {valor}')
#     myValue = valor
#     valorSum = index + rango
#     index += 1
#     if valorSum < len(lista):
#         if myValue in lista[valor:valorSum]:
#             print('Esta dentro')
#         else:
#             print('No esta dentro')
# creo que funcion pero voy a probarlo de otra forma para asegurarme :)

valor_n = 5
memoria = 0
rango = 1
lista = [1, 1, 1, 1, 1]
index = 0
for valor in lista:
    print(f'valor: {valor}')
    myValue = valor
    magic = index + rango
    if magic < valor_n:
        index += 1
        print(f'Busco {myValue} en la lista {lista[index:magic+1]}')
        if myValue in lista[index:magic+1]:
            memoria += 1
            print('Si esta el cabron!')

print(memoria)
# EUREKAAAAAA
