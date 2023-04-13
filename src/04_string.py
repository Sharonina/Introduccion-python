name = 'Sharon'
print(name) # Sharon

last_name = 'Arana'
print(last_name) # Arana

# concatenación de strings
full_name = name + last_name
print(full_name) # SharonArana

full_name = name + " " + last_name
print(full_name) # Sharon Arana

# Se pueden intercalar las comillas para que no de error al utilizar apostrofes
quote = "I'm Sharon"
print(quote) # I'm Sharon

quote2 = 'Ella dijo "Hola"'
print(quote2) # Ella dijo "Hola"

# format: forma de dar estructura a un texto
template = "Hola, mi nombre es " + name + " y mi apellido es " + last_name
print(template) # Hola, mi nombre es Sharon y mi apellido es Arana

template = "Hola, mi nombre es {} y mi apellido es {}".format(name, last_name)
print(template) # Hola, mi nombre es Sharon y mi apellido es Arana

template = f"Hola, mi nombre es {name} y mi apellido es {last_name}"
print(template) # Hola, mi nombre es Sharon y mi apellido es Arana