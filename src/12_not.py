# not
print(not True)  # False
print(not False)  # True

# and
print('NOT AND')

print('True and True > ', not (True and True))  # False
print('True and False > ', not (True and False))  # True
print('False and True > ', not (False and True))  # True
print('False and False > ', not (False and False))  # True

stock = input('Ingresa el número de stock: ')
stock = int(stock)

print(not (stock >= 100 and stock <= 1000))
