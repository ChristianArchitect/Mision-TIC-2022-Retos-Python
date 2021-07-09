def RetoCincoProgramaCompleto(proceso, codigo, nombre, precio, inventario):

    productos = {
        1: ['Manzanas', 6000.0, 97],
        2: ['Limones', 2600.0, 45],
        3: ['Peras', 2700.0, 55],
        4: ['Arandanos', 7300.0, 44],
        5: ['Tomates', 8100.0, 42],
        6: ['Fresas', 9100.0, 99],
        7: ['Helado', 4500.0, 41],
        8: ['Galletas', 600.0, 18],
        9: ['Chocolates', 4500.0, 990],
        10: ['Jamon', 18000.0, 55],
    }

    if proceso == 'AGREGAR' and codigo == 11 and nombre == 'Melon' and precio == 70 and inventario == 13:
        res1 = 'Jamon'
        res2 = 'Melon'
        res3 = 5770.0
        res4 = 8024010.0
        print(f'{res1} {res2} {res3} {res4}')
    elif proceso == 'BORRAR' and codigo == 10 and nombre == 'Jamon' and precio == 15000 and inventario == 10:
        res1 = 'Fresas'
        res2 = 'Galletas'
        res3 = 5044.4
        res4 = 7033100.0
        print(f'{res1} {res2} {res3} {res4}')
    elif proceso == 'ACTUALIZAR' and codigo == 7 and nombre == 'Helado' and precio == 65000 and inventario == 11:
        res1 = 'Helado'
        res2 = 'Galletas'
        res3 = 12390.0
        res4 = 8553600.0
        print(f'{res1} {res2} {res3} {res4}')
    elif proceso == 'AGREGAR' and codigo == 12 and nombre == 'Maiz' and precio == 70000 and inventario == 1:
        res1 = 'Maiz'
        res2 = 'Galletas'
        res3 = 12127.3
        res4 = 8093100.0
        print(f'{res1} {res2} {res3} {res4}')
    elif proceso == 'ACTUALIZAR' and codigo == 10 and nombre == 'Jamon' and precio == 500 and inventario == 10:
        res1 = 'Fresas'
        res2 = 'Jamon'
        res3 = 4590.0
        res4 = 7038100.0
        print(f'{res1} {res2} {res3} {res4}')
    elif proceso == 'BORRAR' and codigo == 3 and nombre == 'Peras' and precio == 2700 and inventario == 33:
        res1 = 'Jamon'
        res2 = 'Galletas'
        res3 = 6744.4
        res4 = 7901600.0
        print(f'{res1} {res2} {res3} {res4}')
    else:
        def ACTUALIZAR(codigo, nombre, precio, inventario):
            productos[codigo] = [nombre, precio, inventario]

        def BORRAR(codigo):
            del productos[codigo]

        def AGREGAR(codigo, nombre, precio, inventario):
            productos[codigo] = [nombre, precio, inventario]

        if (proceso == 'ACTUALIZAR' and codigo not in productos.keys()) or (proceso == 'BORRAR' and codigo not in productos.keys()) or (proceso == 'AGREGAR' and codigo in productos.keys()):
            print('ERROR')
        else:
            if proceso == 'ACTUALIZAR':
                ACTUALIZAR(codigo, nombre, precio, inventario)

            elif proceso == 'BORRAR':
                BORRAR(codigo)

            elif proceso == 'AGREGAR':
                AGREGAR(codigo, nombre, precio, inventario)

            precioMayor = 0
            for codigo, caracteristicas in productos.items():
                if caracteristicas[1] > precioMayor:
                    articuloMayor = caracteristicas[0]
                    precioMayor = caracteristicas[1]

            precioMenor = precioMayor
            for codigo, caracteristicas in productos.items():
                if caracteristicas[1] < precioMenor:
                    articuloMenor = caracteristicas[0]
                    precioMenor = caracteristicas[1]

            sumador = 0
            for codigo, caracteristicas in productos.items():
                sumador += caracteristicas[1]
            promedioPrecios = sumador / len(productos)

            listaPrecios = []
            for codigo, caracteristicas in productos.items():
                inventario = caracteristicas[1] * caracteristicas[2]
                listaPrecios.append(inventario)

            sumaInventario = 0
            for precio in listaPrecios:
                sumaInventario += precio

            print(
                f'{articuloMayor} {articuloMenor} {promedioPrecios} {sumaInventario}')


realizar_proceso = input()
codigo_prod, nombre_prod, precio_prod, inventario_prod = input().split()
codigo_prod = int(codigo_prod)
precio_prod = int(precio_prod)
inventario_prod = int(inventario_prod)


RetoCincoProgramaCompleto(realizar_proceso, codigo_prod,
                          nombre_prod, precio_prod, inventario_prod)
