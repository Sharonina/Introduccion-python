x = 3.3
y = 1.1 + 2.2
# Comparaciones de flotantes

print(x)  # 3.3
print(y)  # 3.3000000000000003

# El resultado es flaso porque no hay la misma precisión
print(x == y)  # False

# Posibles soluciones

# Convertimos y a string y le decimos que solo queremos 2 dígitos
y_str = format(y, '.2g')
print(y_str)  # '3.3'
print(y_str == str(x))  # True

# Forma matemática
print('*' * 10)
print(y, x)  # 3.3000000000000003 3.3

# Se resta x - y para sacar el balor absoluto de ese resultado y compararlo con la tolerancia
tolerance = 0.00001
print(abs(x - y) < tolerance)  # True
