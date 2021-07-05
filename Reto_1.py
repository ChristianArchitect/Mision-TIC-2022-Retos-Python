# Enunciado
'''
Un empleado de una empresa de TV cable desea conocer a cuantó dinero equivalen los descuentos parafiscales exigidos por la ley en relacíon con los pagos que la empresa para la que trabaja le realizan mensualmente. Se ha firmado un contrato que le permite trabajar 48 horas semanales. Con el propósito de verificar el valor total de los descuentos han decidido construir un programa en Python que le permita verificar el valor de su salario antes y después de realizar los descuentos. Después de consultar sobre la normatividad y revisar con detalle su contrato laboral nota que debe tener en cuenta los siguientes aspectos:
-----------------------------------------------------------------------------------------
* El valor de una hora de trabajo normal se obtiene dividiendo el salario base sobre 176
* Las horas extras se liquidan con un recargo del 25% sobre el valor de una hora normal
* Debido a buen desempeño de un empleado la empresa ocasionalmente otorga bonificaciones de 6.5% del salario base.
* El salario total antes de descuentos se calcula como la suma del salario base, más el valor de las horas extras, más las bonificaciones (si las hay)
* Se descontará 2.5% del salario total antes de descuentos para el aporte a pensión
* Se descontará 4% del salario total antes de descuentos para caja de compensación
---------------------------------------------------------------------------
Luego de considerar toda esta información, el empleado decide construir un programa que permita a cualquier empleado de la empresa verificar si los pagos son correctos.

ENTRADA:
El programa recibirá 3 parámetros:
- El salario base del empleado
- La cantidad de horas extras se representa a través de un número entero positivo. En caso de realizar horas extras durante el mes, se ingresará el valor 0.
- Si hubo bonificaciones se ingresará el valor 1, de lo contrario el valor 0
SALIDA:
El programa debe imprimir 2 valores:
- El valor a pagar al empleado luego de realizar los descuentos de ley. El resultado debe imprimirse con un número decimal
- El salario total del empleado antes de descuentos. El resultado debe imprimirse con un número decimal
'''

# start
salario_base, horas_extra, bonificacion = input().split()
salario_base = float(salario_base)
horas_extra = float(horas_extra)
bonificacion = float(bonificacion)

valorHora = salario_base / 176
calculoExtras = 0
if horas_extra > 0:
    calculoExtras = (valorHora + (valorHora * 0.25)) * horas_extra
valorBonificacion = 0
if bonificacion == 1:
    valorBonificacion = salario_base * 0.065
salarioAntesDescuentos = salario_base + calculoExtras + valorBonificacion
descuentoSalud = salarioAntesDescuentos * 0.025
descuentoPension = salarioAntesDescuentos * 0.025
descuentoCompensacion = salarioAntesDescuentos * 0.040
totalPagarEmpleado = salarioAntesDescuentos - \
    descuentoPension - descuentoCompensacion - descuentoSalud
print(f'{salarioAntesDescuentos:.1f} {totalPagarEmpleado:.1f}')
# stop
