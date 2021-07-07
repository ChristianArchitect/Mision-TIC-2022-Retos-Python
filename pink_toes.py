cantRepetidas = 0
contador = 0
while contador < valor_n:
    myCoin = listaMonedas[0]
    del listaMonedas[0]
    if myCoin in listaMonedas:
        cantRepetidas += 1
    contador += 1
print(cantRepetidas)
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
