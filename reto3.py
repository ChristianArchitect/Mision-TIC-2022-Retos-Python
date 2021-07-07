cantidad_registros = int(input())

listaCampeones = []
for registro in range(0, cantidad_registros):
    goles_marcados, goles_recibidos, tarj_amarillas, tarj_rojas, mill_recaudados = input().split()
    goles_marcados = int(goles_marcados)
    goles_recibidos = int(goles_recibidos)
    tarj_amarillas = int(tarj_amarillas)
    tarj_rojas = int(tarj_rojas)
    mill_recaudados = int(mill_recaudados)
    if goles_marcados > 0 or goles_recibidos > 0 or tarj_amarillas > 0 or tarj_rojas > 0 or mill_recaudados > 0:
        if goles_marcados > 100 and goles_recibidos <= 9 and tarj_amarillas <= 5 and tarj_rojas == 0:
            listaCampeones.append(mill_recaudados)
if len(listaCampeones) == 0:
    print('NO DISPONIBLE')
else:
    for campeon in listaCampeones:
        print(campeon)
