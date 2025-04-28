#1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
#(incluyendo ambos extremos), en orden creciente, mostrando un número por línea.
print("NÚMEROS DEL 1 AL 100")

#for numero in range(...) recorre cada número uno por uno.
for numero in range(0, 101): #range(0, 101) genera una secuencia de números que empieza en 0 y llega hasta 100 (el 101 no se incluye).
    print(numero) #print(numero) muestra cada número en una nueva línea.

#//////////////////////////////////#////////////////////////////////////////////////////

#CON WHILE
#Primero, se define la variable numero y se inicializa en 0.
n = 0
#El while verifica si numero es menor o igual a 100.
while numero <= 100:
    print(numero)
    numero += 1 #En cada vuelta del bucle, imprime el valor actual de numero y luego suma 1.
    
    
#2) Desarrolla un programa que solicite al usuario un número entero y
# determine la cantidad de dígitos que contiene.

# # Convirtiendo el número a cadena (str)
# print("Cantidad de digitos en un numero entero")

# numero = int(input("Ingrese un úmero entero: "))
# cantidad_de_digitos = len(str(numero))
# print("La cantidad de digitos es:",cantidad_de_digitos)

#Usando operaciones matemáticas
# Definimos el número al que queremos contarle los dígitos
numero = int(input("Ingrese un nro entero: "))
cantidad_de_digitos = 0 # Inicializamos el contador de dígitos en 0

while numero > 0: # Mientras el número sea mayor que 0
    numero = numero // 10  # Hacemos una división entera para eliminar el último dígito
    cantidad_de_digitos += 1  # Aumentamos el contador de dígitos en 1
    # Cuando terminamos el bucle, mostramos la cantidad total de dígitos
print(cantidad_de_digitos)


# 3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
# dados por el usuario, excluyendo esos dos valores.

# Pedimos los dos valores al usuario
valor1 = int(input("Ingrese el primer número: "))
valor2 = int(input("Ingrese el segundo número: "))

# Aseguramos que valor1 sea menor que valor2
if valor1 > valor2:
    valor1, valor2 = valor2, valor1  # Intercambiamos los valores si están al revés

# Inicializamos la suma en 0
suma = 0

# Recorremos los números entre valor1 y valor2, excluyéndolos
for numero in range(valor1 + 1, valor2):
    suma += numero  # Sumamos cada número

# Mostramos el resultado
print("La suma de los números entre", valor1, "y", valor2, "es:", suma)


# 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
# secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
# un 0.

numero = int(input("Ingrese un nro entero: "))  # Pedimos el primer número
acu = 0  # Inicializamos el acumulador

while numero != 0:  # Mientras el número ingresado no sea 0
    acu += numero  # Acumulamos el valor
    numero = int(input("Ingrese otro nro entero: "))  # Pedimos el siguiente número y lo asignamos a 'numero'

print("El total acumulado es:", acu)  # Mostramos el resultado final


# 5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
# programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

import random  # Importamos el módulo random para generar números aleatorios

# Generamos un número aleatorio entre 0 y 
#random.randint(0, 9): Esto genera un número aleatorio entre 0 y 9 (incluyendo ambos).
numero_aleatorio = random.randint(0, 9)

# Inicializamos la variable de intentos
intentos = 0 #intentos: Es un contador que aumenta cada vez que el usuario hace un intento.
adivinado = False  # Variable para controlar si el usuario adivinó el número
# Comenzamos el juego
print("Adivina el número entre 0 y 9.")

# Bucle que se repite hasta que el usuario adivine el número
#while True: El bucle continuará pidiendo al usuario que ingrese un número hasta que adivine el correcto.
while not adivinado:
    # Pedimos al usuario que ingrese un número
    intento_usuario = int(input("Introduce tu intento: "))
    
    # Aumentamos el contador de intentos
    intentos += 1
    
    # Verificamos si el intento es correcto
    if intento_usuario == numero_aleatorio:
        print(f"¡Felicidades! Adivinaste el número en {intentos} intentos.")
        break  # Terminamos el juego si adivina correctamente
    elif intento_usuario < numero_aleatorio:
        print("El número es mayor. Intenta nuevamente.")
    else:
        print("El número es menor. Intenta nuevamente.")
        
        
        
#6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
#entre 0 y 100, en orden decreciente.
# Usamos range para contar de 100 a 0, con paso de -2 (para solo mostrar pares)
for i in range(100, 0, -2):# Comienza en 100, termina en 0, y cuenta hacia atrás con paso -2
     print(i)
    
#range(100, -1, -2): El primer valor 100 es el inicio del rango,
# el segundo valor -1 es el límite (sin incluirlo, por eso es -1 y no 0),
# y el -2 es el paso, que indica que vamos a contar de 2 en 2, de forma decreciente.


# 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
# número entero positivo indicado por el usuario.

suma = 0

# Pedimos al usuario un número entero positivo
numero = int(input("Ingresa un número entero positivo: "))

# Verificamos que el número sea positivo
if numero <= 0:
    print("Por favor, ingresa un número entero positivo.")
else:
    # Recorremos los números desde 0 hasta el número ingresado (sin incluirlo)
    for i in range(0, numero):
        suma += i  # Sumamos cada número

    print("La suma es de:", suma)



#8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
# programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
# negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
# menor, pero debe estar preparado para procesar 100 números con un solo cambio).


# Inicializar los contadores
pares = 0
impares = 0
positivos = 0
negativos = 0

# Número total de entradas a procesar
total_numeros = 100  # Cambiar este valor para probar con una cantidad menor

# Bucle para ingresar los números
for i in range(total_numeros):
    # Pedir al usuario que ingrese un número entero
    numero = int(input(f"Ingrese el número {i+1}: "))
    
    # Verificar si el número es par o impar
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1
    
    # Verificar si el número es positivo o negativo
    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1

# Mostrar los resultados
print(f"\nCantidad de números pares: {pares}")
print(f"Cantidad de números impares: {impares}")
print(f"Cantidad de números positivos: {positivos}")
print(f"Cantidad de números negativos: {negativos}")



# 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la 
# media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe 
# poder procesar 100 números cambiando solo un valor).

# Inicializar la suma
suma = 0

# Número total de entradas a procesar
total_numeros = 100  # Cambiar este valor para probar con una cantidad menor

# Bucle para ingresar los números
for i in range(total_numeros):
    numero = int(input(f"Ingrese el número {i+1}: "))
    suma += numero

# Calcular la media
media = suma / total_numeros

# Mostrar el resultado
print(f"\nLa media de los {total_numeros} números ingresados es: {media}")


# Pedir al usuario que ingrese un número
numero = input("Ingrese un número: ")

# Invertir el número usando slicing
numero_invertido = numero[::-1]

# Mostrar el resultado
print(f"El número invertido es: {numero_invertido}")

# Se usa input() para que el número sea tratado como texto (string) y así poder invertirlo fácilmente.

# [::-1] es una forma rápida de invertir un string en Python.

# Luego se muestra el número invertido.