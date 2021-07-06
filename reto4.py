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

listaMonedas = [1, 2, 3, 1, 2]
maximo = 3
encontrado = 0
contador = 0
iterador = 0
for numero in listaMonedas:
    nuevaLista = listaMonedas[numero:numero+maximo]
    print(nuevaLista)
    if numero in nuevaLista:
        print(f'{numero} esta en la lista')
