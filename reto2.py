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
