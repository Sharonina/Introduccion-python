lives = 3
print(lives) # 3
print(type(lives)) # int

temperatura = 12.12
print(type(temperatura)) # float

# asignando nuevamente un valor
lives = 2
print(lives) # 2

# resolviendo operación matemática
lives = 12 + 15
print(lives) # 27

# se pueden reutilizar valores también
lives = lives - 1
print(lives) # 26

lives -= 1
print(lives) # 25

lives -= 5
print(lives) #20

lives += 5
print(lives) #25

# Python convierte números muy grandes o muy pequeños a notación científica
number_a = 45000000000000000000.1
print(number_a) # 4.5e+19

number_b = 0.0000000000000000001
print(number_b) # 1e-19