# Enunciado
# Reto 5: Inventario para pequeñas superficies
'''
Una tienda de pequeñas superficies vende diferentes productos, usualmente frutas, dulces y algunos tipos de carne. Con el propósito de mejorar el control sobre las ventas y el inventario de la tienda, el administrador decide mandar a construir una aplicación que le permita almacenar la información de los productos y realizar algunos cálculos sobre los datos.
En la primera parte del reto se debe construir una base de datos que almacene la información de los productos disponibles en la tienda. Debido a que el administrador no cuenta con un servidor de base de datos, solicita que temporalmente la base de datos sea representada mediante un diccionario de Python llamado productos que tendrá por llave el código del producto y por valor una lista formada por los atributos: nombre, precio e inventario. La Tabla 1 presenta los productos disponibles a la fecha.
Para simular de una manera más realista la base de datos, es necesario construir 3 funciones que representen las operaciones de: AGREGAR, ACTUALIZAR y BORRAR los productos disponibles. Se debe implementar una función independiente por cada una de las acciones mencionadas. En este caso, para poder realizar las operaciones de ACTUALIZAR o BORRAR es necesario especificar todos los atributos del producto.
Adicionalmente, el administrador está interesado en analizar los datos de los productos disponibles y conocer: el nombre del producto con el precio mayor; el nombre del producto con el precio menor; el promedio de precios de todos los productos y el valor total del inventario a la fecha. Este último se obtiene multiplicando el precio de cada producto por el inventario disponible y luego sumando todos los resultados. Por ejemplo, al calcular estos 4 valores para los datos disponibles en la Tabla 1 obtendríamos :
Producto precio mayor: Jamon
Producto precio menor: Galletas
Promedio de precios: 6340.0
Valor del inventario: 8050100.0
'''
# ENTRADA
'''
Cada uno de los casos de prueba estará compuesto por dos líneas.
La primera línea estará formada por una cadena de texto que identifica la operación a realizar. En este caso, las operaciones validas son:
ACTUALIZAR.
BORRAR.
AGREGAR.
La segunda línea estará formada por 4 valores (código, nombre, precio, inventario) que representan el producto sobre el cual se quiere realizar la operación.
En el caso de la operación ACTUALIZAR la segunda línea debe contener el código y los nuevos valores del producto.
En el caso de la operación BORRAR se deben especificar todos los atributos del producto a eliminar.
'''
# SALIDA
'''
	La salida estará representada por una única línea formada por cuatro valores:
Nombre del producto con el precio mayor.
Nombre delproducto con el precio menor.
Promedio de precios.
Valor del inventario.
Estos 4 valores deben imprimirse después de realizar las operaciones solicitadas en la entrada de datos.
Los valores numéricos deben imprimirse con un número decimal.
En caso de solicitar ACTUALIZAR o BORRAR un producto que no existe (es decir, que el código del producto no se encuentra en la base de datos), se debe imprimir 'ERROR'.
En caso de solicitar AGREGAR un producto cuyo código ya existe en la base de datos se debe imprimir 'ERROR'.
'''

# 1.Construir una base de datos, probablemente con un diccionario con listas anidadas
# la clave es el codigo del producto y el valor es una lista con los atributos del producto
# 2. Construir tres funciones que representen:
# AGREGAR
# ACTUALIZAR
# BORRAR
# 3.Para las funciones de ACTUALIZAR o BORRAR es necesario especificar todos los atributos del producto
# 4.Buscar el nombre del producto con el precio mayor
# 5.Buscar el nombre del producto con el precio menor
# 6.Calcular el promedio de precios de todos los productos
# 7.Calcular el valor total del inventario a la fecha

# BASE DE DATOS
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


def ACTUALIZAR():
    pass


def BORRAR():
    pass


def AGREGAR():
    pass


# ENTRADAS
realizar_proceso = input()  # AGREGAR - BORRAR - ACTUALIZAR
codigo_prod, nombre_prod, precio_prod, inventario_prod = input().split()
codigo_prod = int(codigo_prod)
precio_prod = float(precio_prod)
inventario_prod = int(inventario_prod)

if realizar_proceso == 'ACTUALIZAR':
    ACTUALIZAR()
elif realizar_proceso == 'BORRAR':
    BORRAR()
elif realizar_proceso == 'AGREGAR':
    AGREGAR()

# calcular producto mayor, producto menor y promedio
precioMayor = 0
for producto in productos
