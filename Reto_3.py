# Enunciado
# Reto 3: ¡El campeón es…!
'''
La liga local de fútbol de Macondo con el pasar del tiempo se ha convertido en la liga más competitiva del planeta fútbol. La característica especial que tiene esta liga es que puede otorgar más de un campeón cada temporada, lo cual motiva a los equipos a ser mejores partido a partido. Sin embargo, pese a que puede haber más de un equipo campeón, ser campeón es un logro realmente difícil.
Para hacerse merecedor del Trofeo 'José Arcadio Buendía' los equipos participantes deben cumplir los siguientes requerimientos durante el torneo:
Anotar más de 100 goles.
Haber recibido 9 goles o menos.
Para honrar el juego limpio en el torneo un equipo puede haber recibido máximo 5 tarjetas amarillas. La sexta tarjeta amarilla acaba con la ilusión de ser campeones.
Un total de 0 tarjetas rojas.
Los organizadores de la liga han depositado toda su confianza en usted para determinar qué equipos saldrán campeones esta temporada, así que debe construir el software que procesará los datos de las bases de datos registradas en el sistema.Su misión es crear un programa en Python que permita mostrarle a la organización del torneo la lista de los equipos que al finalizar el torneo cumplen con todos los requerimientos y por supuesto el valor recolectado por cada equipo por concepto de boletería. Este último valor está dado en millones de pesos macondianos (Moneda local).
'''
# ENTRADA
'''
La entrada estará conformada por N + 1 líneas:
La primera línea recibirá un número N que equivale a la cantidad de registros en la base de datos de la liga. Cada registro representa las estadísticas de un equipo.
Cada una de las siguientes N líneas estará formada por 5 números separados por espacios que representan las diferentes estadísticas de un equipo. Por ejemplo,la fila 105 8 5 0 20 representa un equipo que al final de la temporada anotó 105 goles, recibió 8 goles en contra,5 tarjetas amarillas y 0 tarjetas rojas. Además el equipo recaudó 20 millones de pesos macondianos (moneda local).
'''
# SALIDA
'''
El programa imprimirá el valor recaudado por cada uno de los equipos campeones que cumplen con los criterios de la liga.
Si no existe ningún registro en la base de datos que cumpla los criterios de la liga, el programa imprimirá 'NO DISPONIBLE'.
'''

# start
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
# stop
