# Tipos de datos

# String: Cadenas de texto, se asigna con comillas simples y sencillas
my_name = 'Sharon'
my_name = "Sharon"

print(type(my_name)) # class 'str' : clase de tipo string

# Numbers: Enteros, se asigna sin ''
my_age = 26
print(type(my_age)) # class 'int'

# Boolean: True/False, la primer letra debe ir en mayúscula
is_single = True
print(type(is_single)) # class 'bool'

# Siempre que se recibe algo de un input, se recibe como string así sea numero o texto
my_age = input('¿Cuál es tu edad?')
print('my age >', my_age)
print(type(my_age)) # class 'str'
