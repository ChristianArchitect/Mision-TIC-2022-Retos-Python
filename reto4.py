valor_n, valor_k = input().split()
valor_n = int(valor_n)
valor_k = int(valor_k)
lista_entrada = input().split()
listaMonedas = []
for moneda in lista_entrada:
    if moneda != ' ':
        m = int(moneda)
        listaMonedas.append(m)

listaMonedas2 = listaMonedas[:]
cantRepetidas = 0
contador = 0
while contador < valor_n:
    myCoin = listaMonedas[0]
    del listaMonedas[0]
    if myCoin in listaMonedas:
        cantRepetidas += 1
    contador += 1

memoria = 0
index = 0
for valor in listaMonedas2:
    myValue = valor
    magic = index + valor_k
    if magic <= valor_n:
        index += 1
        if myValue in listaMonedas2[index:magic+1]:
            memoria += 1

print(f'{cantRepetidas} {memoria}')
