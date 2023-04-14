# Transformaciones de tipos

name = 'Sharon'
print(type(name)) #str

# Se pueden realizar transformaciones de manera dinámica a los datos
name = 11
print(type(name)) # int

name = True
print(type(name)) # bool

# Debido a que no se pueden sumar str + int, se debe transformar el tipo de dato para usarlo
age = 12
print('mi edad es ' + str(age))
# al realizarlo con format, NO es necesario hacer la transformación, puesto que format la realiza por default
print(f'Mi edad es {age}')

# obteniendo datos de un input
age = input('Escribe tu edad > ')
print(type(age)) # str
age = int(age)
age += 10
print(f'Tu edad en 10 años será {age}')

