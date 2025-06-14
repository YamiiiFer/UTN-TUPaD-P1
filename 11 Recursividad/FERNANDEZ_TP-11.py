#1) Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa
#función para calcular y mostrar en pantalla el factorial de todos los números enteros
#entre 1 y el número que indique el usuario

#1) Factorial de un número
#El factorial de un número n es:
#n! = n × (n-1) × (n-2) × ... × 1
#
#Caso base: factorial(1) = 1
#Paso recursivo: factorial(n) = n × factorial(n - 1)
#
#📌 Además, tenés que mostrar los factoriales de 1 hasta el número que ingresa el usuario.

# Función recursiva que calcula el factorial de un número
def factorial(n):
    if n <= 0:
        # Caso base: el factorial de 0 es 1 por definición
        return 1
    else:
        # Paso recursivo: n * factorial de (n - 1)
        return n * factorial(n - 1)

# Pedimos al usuario un número entero positivo
numero = int(input("Ingrese un número entero positivo: "))

# Validamos que no sea negativo
if numero < 0:
    print("No se puede calcular el factorial de un número negativo.")
else:
    # Mostramos los factoriales desde 1 hasta el número ingresado
    print(f"\nFactoriales desde 1 hasta {numero}:\n")
    for i in range(1, numero + 1):
        print(f"{i}! = {factorial(i)}")

#2) Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición
#indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario
#especifique.


# Función recursiva para calcular el número de Fibonacci en la posición n
def fibonacci(n):
    if n == 0:
        return 0  # Caso base 1
    elif n == 1:
        return 1  # Caso base 2
    else:
        # Paso recursivo: suma de los dos anteriores
        return fibonacci(n - 1) + fibonacci(n - 2)

# Pedimos al usuario que ingrese la cantidad de términos que quiere ver
posicion = int(input("¿Hasta qué posición de la serie Fibonacci querés mostrar? (número entero ≥ 0): "))

# Validamos que el número no sea negativo
if posicion < 0:
    print("Por favor, ingresá un número positivo.")
else:
    print(f"\nSerie de Fibonacci hasta la posición {posicion}:")
    for i in range(posicion + 1):  # desde 0 hasta 'posicion' inclusive
        print(f"fibo({i}) = {fibonacci(i)}")


#3) Crea una función recursiva que calcule la potencia de un número base elevado a un
#exponente, utilizando la fórmula 𝑛
#𝑚 = 𝑛 ∗ 𝑛(𝑚−1)
#. Prueba esta función en un algoritmo general.

# Función recursiva para calcular la potencia
def potencia(base, exponente):
    if exponente == 0:
        return 1  # Caso base: cualquier número a la 0 es 1
    else:
        # Paso recursivo: base * potencia(base, exponente - 1)
        return base * potencia(base, exponente - 1)

# Pedimos los datos al usuario
base = int(input("Ingresá la base: "))
exponente = int(input("Ingresá el exponente (entero positivo): "))

# Validamos que el exponente no sea negativo
if exponente < 0:
    print("No se puede calcular la potencia con exponente negativo usando esta función.")
else:
    resultado = potencia(base, exponente)
    print(f"\n{base}^{exponente} = {resultado}")
    


#4) Crear una función recursiva en Python que reciba un número entero positivo en base
#decimal y devuelva su representación en binario como una cadena de texto.
#Cuando representamos un número en binario, lo expresamos usando solamente ceros (0) y
#unos (1), en base 2. Para convertir un número decimal a binario, se puede seguir este
#procedimiento:
#1. Dividir el número por 2.
#2. Guardar el resto (0 o 1).
#3. Repetir el proceso con el cociente hasta que llegue a 0.
#4. Los restos obtenidos, leídos de abajo hacia arriba, forman el número binario.
#🧠Ejemplo:
#Convertir el número 10 a binario:
#10 ÷ 2 = 5 resto: 0
#5 ÷ 2 = 2 resto: 1
#2 ÷ 2 = 1 resto: 0
#1 ÷ 2 = 0 resto: 1
#Leyendo los restos de abajo hacia arriba: 1 0 1 0 → El resultado binario es "1010".

def decimal_a_binario(n):
    # Caso base: si el número es 0, devolvemos cadena vacía para que no haya un "0" inicial extra
    if n == 0:
        return ""
    else:
        # Se llama recursivamente con el cociente de la división entera entre 2
        # Y se concatena el resto de la división (0 o 1) como string al final
        return decimal_a_binario(n // 2) + str(n % 2)

# Ejemplo de uso:
numero = int(input("Ingrese un número entero positivo: "))
if numero == 0:
    print("El número binario es: 0")
elif numero > 0:
    binario = decimal_a_binario(numero)
    print(f"El número binario es: {binario}")
else:
    print("Por favor, ingrese un número entero positivo.")


#5) Implementá una función recursiva llamada es_palindromo(palabra) que reciba una
#cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no
#lo es.
# Requisitos:
#La solución debe ser recursiva.
#No se debe usar [::-1] ni la función reversed().

def es_palindromo(palabra):
    # Caso base: si la palabra tiene 0 o 1 letra, es palíndromo
    if len(palabra) <= 1:
        return True
    # Comparamos primera y última letra
    if palabra[0] != palabra[-1]:
        return False
    # Llamada recursiva con la palabra sin la primera y la última letra
    return es_palindromo(palabra[1:-1])

# Pedimos una palabra al usuario
entrada = input("Ingrese una palabra (sin espacios ni tildes): ").lower()

# Verificamos si es un palíndromo
if es_palindromo(entrada):
    print("✅ Es un palíndromo.")
else:
    print("❌ No es un palíndromo.")


#6) Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un
#número entero positivo y devuelva la suma de todos sus dígitos.
# Restricciones:
#No se puede convertir el número a string.
#Usá operaciones matemáticas (%, //) y recursión.
#Ejemplos:
#suma_digitos(1234) → 10 (1 + 2 + 3 + 4)
#suma_digitos(9) → 9
#suma_digitos(305) → 8 (3 + 0 + 5)

def suma_digitos(n):
    # Caso base: si el número tiene un solo dígito
    if n < 10:
        return n
    else:
        # Sumamos el último dígito y llamamos recursivamente con el resto
        return (n % 10) + suma_digitos(n // 10)

# Pedir al usuario un número entero positivo
numero = int(input("Ingrese un número entero positivo: "))

# Validar que sea positivo
if numero >= 0:
    resultado = suma_digitos(numero)
    print(f"La suma de los dígitos de {numero} es: {resultado}")
else:
    print("Por favor, ingrese un número entero positivo.")


#7) Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n
#bloques, en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al
#último nivel con un solo bloque.
#Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el
#nivel más bajo y devuelva el total de bloques que necesita para construir toda la
#pirámide.
# Ejemplos:
#contar_bloques(1) → 1 (1)
#contar_bloques(2) → 3 (2 + 1)
#contar_bloques(4) → 10 (4 + 3 + 2 + 1)

def contar_bloques(n):
    # Caso base: si hay un solo nivel, solo se necesita 1 bloque
    if n == 1:
        return 1
    else:
        # Se suman los bloques del nivel actual con los del nivel de arriba
        return n + contar_bloques(n - 1)

# Programa principal
nivel_inferior = int(input("Ingrese la cantidad de bloques del nivel más bajo: "))

# Validación básica
if nivel_inferior >= 1:
    total = contar_bloques(nivel_inferior)
    print(f"Total de bloques necesarios para construir la pirámide: {total}")
else:
    print("Por favor, ingrese un número mayor o igual a 1.")

#8) Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un
#número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces
#aparece ese dígito dentro del número.
# Ejemplos:
#contar_digito(12233421, 2) → 3
#contar_digito(5555, 5) → 4
#contar_digito(123456, 7) → 0 

def contar_digito(numero, digito):
    # Caso base: si el número tiene un solo dígito
    if numero == 0:
        return 0
    else:
        # Si el último dígito es igual al que buscamos, sumamos 1
        coincidencia = 1 if numero % 10 == digito else 0
        # Llamada recursiva con el número sin el último dígito
        return coincidencia + contar_digito(numero // 10, digito)

# Programa principal
numero = int(input("Ingrese un número entero positivo: "))
digito = int(input("Ingrese un dígito del 0 al 9: "))

# Validación básica
if numero >= 0 and 0 <= digito <= 9:
    resultado = contar_digito(numero, digito)
    print(f"El dígito {digito} aparece {resultado} veces en el número {numero}.")
else:
    print("Entrada inválida. Asegúrese de ingresar un número positivo y un dígito entre 0 y 9.")
