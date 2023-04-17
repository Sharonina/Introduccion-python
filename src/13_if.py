if True:
    print('Debería ejecutarse')

if False:
    print('Nunca se ejecuta')

# uso de if
pet = input('Cual es tu mascota favorita: ')
if pet == 'perro':
    print('Genial, tienes buen gusto')

if pet == 'gato':
    print('Suerte con tu mascota')

# uso de if y else
stock = int(input('Digita el stock: '))

if stock >= 100 and stock <= 1000:
    print('El stock es correcto')
else:
    print('El stock es incorrecto')

# uso de elif
color = input('Que color te gusta: ')

if color == 'rosa':
    print('Genial')
elif (color == 'azul'):
    print('Buu')
else:
    print('no te gusta ningun color interesante')
