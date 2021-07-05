# Enunciado
# Reto 2: Multas por exceso de velocidad
'''
Debido a la alta accidentalidad presentada en el último año en las carreteras del territorio nacional, el Gobierno Colombiano ha decidido implementar controles que permitan sancionara a los conductores que no respeten los límites de velocidad establecidos por los organismos de control. Con este fin, el Ministerio de Transporte ha decidido implementar radares de tramo en las carreteras con mayores índices de accidentalidad en el país.

Los radares de tramo funcionan colocando dos cámaras en dos puntos alejados de una carretera con el fin de comprobar cuánto tiempo tarda un conductor recorrer dicho tramo. Estos radares no mide la velocidad de paso, sino el tiempo de paso representado como la velocidad media de un conductor en un trayecto con una longitud determinada.

Formalmente, los radares de tramo se basan en el teorema de Lagrange (también conocido como el teorema de valor medio o de Bonnet-Lagrange), el cual nos dice que dice tenemos una función continua en un intervalo cerrado, y derivable en un intervalo abierto, entonces algún punto de ese intervalo abierto la función tendrá una derivada instantánea igual a la pendiente media de la curva en el intervalo cerrado.

Aunque estos conceptos pueden asustar en un principio, su interpretación es muy simple: si hacemos un viaje desde Bogotá a Tunja y nuestra velocidad media es de 100 Km/h, necesariamente en algún punto del trayecto nuestra velocidad habrá sido de 100 Km/h. Esto quiere decir que si la velocidad media supera la velocidad máxima permitida, gracias al teorema anterior, sabremos que en algún punto del trayecto se superó la velocidad máxima permitida. Por ejemplo, si colocamos las cámaras separadas 10 Km en un tramo cuya velocidad máxima es de 110 Km/h, y un conductor tarda 5 minutos en ser visto por la segunda cámara, sabremos que su velocidad media ha sido de 120 Km/h, y por tanto, en algún sitio ha superado la velocidad permitida.

Usted hace parte del equipo de desarrollo encargado de construir el software que procesará los datos registrados por las cámaras.Su misión es crear un programa en Python que permita saber si un conductor debe ser multado o no.
'''
# Datos entrada y salida
'''
ENTRADA:
El programa recibirá 3 parámetros:
1. La distancia en metros que separa dos cámaras.
2. La velocidad máxima permitida en ese tramo en (Km/h).
3. El tiempo en segundos que tarda el conductor en recorrer el trayecto.

SALIDA:
El programa imprimirá una línea con dos valores: el primer valor corresponde a la velocidad media del trayecto evaluado en (km/h) y con un número decimal; el segundo valor indicará sí el conductor debe ser multado o no. Se debe considerar lo siguiente:
Imprimirá OK si el conductor no superó la velocidad máxima.
Imprimirá MULTA si se superó la velocidad máxima en menos de un 20% de la velocidad permitida.
Imprimirá CURSO si la velocidad fue superada en un 20% o más de la velocidad permitida. En este caso además de la multa deberá realizar un curso de sensibilización.
Debido a que los sistemas pueden fallar y registrar valores errados (por ejemplo, indicando que el tiempo que ha tardado el conductor es negativo). En esos casos, se deberá imprimir únicamente ERROR.
'''
# start
distancia_metros, velocidad_permitida, tiempo_seg = input().split()
distancia_metros = float(distancia_metros)
velocidad_permitida = float(velocidad_permitida)
tiempo_seg = float(tiempo_seg)

if distancia_metros < 0 or velocidad_permitida < 0 or tiempo_seg < 0:
    print('ERROR')
else:
    velocidadMaxima = ((distancia_metros / tiempo_seg) * 3600) / 1000
    if velocidadMaxima > velocidad_permitida:
        calculo20 = velocidad_permitida * 0.20
        velocidadMULTA = velocidad_permitida + calculo20
        if velocidadMaxima >= velocidadMULTA:
            print(f'{round(velocidadMaxima, 1)} CURSO')
        else:
            print(f'{round(velocidadMaxima, 1)} MULTA')
    else:
        print(f'{round(velocidadMaxima, 1)} OK')
# stop
