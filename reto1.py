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
totalPagarEmpleado = salarioAntesDescuentos - descuentoPension - descuentoCompensacion - descuentoSalud
print(f'{salarioAntesDescuentos:.1f} {totalPagarEmpleado:.1f}')
