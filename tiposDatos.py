# Autor: LozanoSoft

# ---
# Tipos de datos simples
# ---

cadenaCaracteres = 'hola mundo 12345' # Uno o más caracteres
caracter = 'h' # Un solo caracter
numEntero = 98 # Número entero
numFlotante = 3.1415926 # Número con punto decimal
floatPresicionDoble = 3.1415926535 # Número con punto decimal
varBooleana = True # Indicador/Switch -> 0, 1

print('Cadena de caracteres: ' + cadenaCaracteres)
print('Caracter: ' + caracter)
print('Número entero: ' + str(numEntero))
print('Número con punto decimal: ' + str(numFlotante))
print('Número con punto decimal: ' + str(floatPresicionDoble))
print('Variable booleana: ' + str(varBooleana) + '\n')

# Valores decimales y booleanos pueden ser convertidos a enteros

print('Conversión de punto decimal a entero: ' + str(int(numFlotante)))
print('Conversión de booleano a entero: ' + str(int(varBooleana)))

# Valores enteros y booleanos pueden ser convertidos a decimales

print('Conversión de entero a punto decimal: ' + str(float(numEntero)))
print('Conversión de booleano a punto decimal: ' + str(float(varBooleana)))

# Conversiones ASCII

print('Conversión de num. entero a caracter: ' + chr(numEntero))
print('Conversión de caracter a num. entero: ' + str(ord(caracter)) + '\n')

# ---
# Tipos de datos complejos
# ---

# Listas

# Conjunto de elementos dinámico (puede modificarse)
# Comienza desde el índice 0
# Pueden agruparse valores de distintos tipos de datos

lista = [10, 'hola mundo', 'k', 40.89]
lista[1] += ' digital'

print(lista)
print(lista[:])
print(lista[0])
print(lista[3])
print(str(lista[:-1]) + '\n')

sublista = lista[1:3] # sublista
print(str(sublista) + '\n')

# Tuplas

# Conjunto de elementos estático (no puede modificarse)
# Comienza desde el índice 0
# Pueden agruparse valores de distintos tipos de datos

tupla = (6, 15, 'Hola mundo', 'Programando con LozanoSoft')

print(tupla)
print(tupla[:])
print(tupla[0])
print(tupla[3])
print(str(tupla[:-1]) + '\n')

subtupla = tupla[1:3] # subtupla

print(str(subtupla) + '\n')

# Conversiones

print(tuple(lista)) # Lista a tupla
print(str(list(tupla)) + '\n') # Tupla a lista

# Diccionario

# Cada elemento se compone de un par clave-valor
# Es posible acceder a un valor utilizando su clave, pero no al revés
# No se pueden repetir las claves para elementos distintos
# Es dinámico

diccionario = {'Llave':'Valor', 'NIP':2154785}

print(diccionario)
print(diccionario['Llave'])
print(diccionario['NIP'])