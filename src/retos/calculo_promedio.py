'''
Dadas 3 cantidades de presupuesto mensual, calcular el promedio
'''
# opción 1
enero = 1000
febrero = 1500
marzo = 2000

prespuesto = (enero + febrero + marzo)/3
print(prespuesto) # 1500

# opción 2
mes1 = int(input('¿Cuál es tu presupuesto del mes 1?'))
mes2 = int(input('¿Cuál es tu presupuesto del mes 2?'))
mes3 = int(input('¿Cuál es tu presupuesto del mes 3?'))

prespuestoTotal = (mes1 + mes2 + mes3 )/3
print(prespuestoTotal)
