#Crear una función llamada imprimir_hola_mundo que imprima por
#pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
#programa principal.

#Definir funcion

def imprimir_hola_mundo():
    print ("Hola Mundo!")  # esto es lo que hace la función
# Llamada a la función desde el programa principal:
imprimir_hola_mundo()

#Crear una función llamada saludar_usuario(nombre) que reciba
#como parámetro un nombre y devuelva un saludo personalizado.
#Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver: “Hola Marcos!”. Llamar a esta función desde el programa
#principal solicitando el nombre al usuario

def saludar_usuario(nombre):
    return (f"Hola {nombre}!")

#Programa principal

nombre = input("Ingrese su nombre: ")
print(saludar_usuario(nombre))


#Crear una función llamada informacion_personal(nombre, apellido,
#edad, residencia) que reciba cuatro parámetros e imprima: “Soy
#[nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pedir los datos al usuario y llamar a esta función con los valores ingresados.

def informacion_personal(nombre, apellido, edad, residencia):
    return f"Me llamo {nombre} {apellido}, tengo {edad} años y soy de {residencia}"

#Programa principal
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
residencia = input("Ingrese su residencia: ")

mensaje = informacion_personal(nombre, apellido, edad, residencia)

print(mensaje)



#Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y devuelva el área del círculo. 
#calcular_perimetro_circulo(radio) que reciba el radio como parámetro y devuelva el perímetro del círculo. 
#Solicitar el radio al usuario y llamar ambas funciones para mostrar los resultados.

import math  # Importar el módulo para usar math.pi

# Defino las funciones
def calcular_area_circulo(radio):
    return math.pi * (radio ** 2)

def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio

# Programa principal
radio = float(input("Ingrese el radio: "))

# Calcular el área y el perímetro usando las funciones
area = calcular_area_circulo(radio)
perimetro = calcular_perimetro_circulo(radio)

# Mostrar los resultados
print(f"El área del círculo es {area:.2f} y el perímetro es {perimetro:.2f}")



#Crear una función llamada segundos_a_horas(segundos) que reciba
#una cantidad de segundos como parámetro y devuelva la cantidad
#de horas correspondientes. Solicitar al usuario los segundos y mostrar el resultado usando esta función.

# Definición de función
def segundos_a_horas(segundos):
    return segundos * (1 / 3600)

# Programa principal
segundos = int(input("Ingrese la cantidad de segundos que desea convertir a horas: "))

horas = segundos_a_horas(segundos)

print("CONVERSIÓN:", segundos, "segundos son", round(horas, 2), "horas.")


#Crear una función llamada tabla_multiplicar(numero) que reciba un
#número como parámetro y imprima la tabla de multiplicar de ese
#número del 1 al 10. Pedir al usuario el número y llamar a la función.

# Definición de función
def tabla_multiplicar(numero):
    for i in range(1, 11 ):
        print(f"{numero} x {i} = {numero * i}")
# Programa principal
numero = int(input("Ingrese un número para mostrar su tabla de multiplicar: "))
tabla_multiplicar(numero)


#Crear una función llamada operaciones_basicas(a, b) que reciba
#dos números como parámetros y devuelva una tupla con el resultado de sumarlos, restarlos, multiplicarlos y dividirlos.
#Mostrar los resultados de forma clara.

# Definición de la función
def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    # Controlamos que no se divida por 0
    if b != 0:
        division = a / b
    else:
        division = "No se puede dividir por cero"
    
    return (suma, resta, multiplicacion, division)  # Tupla con los 4 resultados

# Programa principal
a = float(input("Ingrese el primer número: "))
b = float(input("Ingrese el segundo número: "))

# Guardamos la tupla en una variable
resultados = operaciones_basicas(a, b)

# Mostramos cada uno de forma clara
print("Resultados:")
print("Suma:", resultados[0])
print("Resta:", resultados[1])
print("Multiplicación:", resultados[2])
print("División:", resultados[3])


#Crear una función llamada calcular_imc(peso, altura) que reciba el
#peso en kilogramos y la altura en metros, y devuelva el índice de
#masa corporal (IMC). Solicitar al usuario los datos y llamar a la función para mostrar el resultado con dos decimales.

#Definicion de la funcion

def calcular_imc(peso, altura):
    return peso / (altura**2)

#Programa principal

peso = float(input("Ingrese el peso en kilogramos: "))
altura = float(input("Ingrese la altura en metros: "))

imc = calcular_imc(peso, altura)

print(f"Su IMC es: {imc:.2f}")


#Crear una función llamada celsius_a_fahrenheit() celsiusque reciba
#una temperatura en grados Celsius y devuelva su equivalente en
#Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
#resultado usando la función.

#Definir funciones

def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

#Programa principal

celsius = float(input("Ingrese la temperatura en grados Celsius: "))
fahrenheit = celsius_a_fahrenheit(celsius)

print(f"{celsius}C equivale a {fahrenheit: .2f} F")



#Crear una función llamada calcular_promedio(a, b, c) que reciba tres números como parámetros y devuelva el promedio de ellos.
#Solicitar los números al usuario y mostrar el resultado usando esta función.

#Definir funciones

def calcular_promedio(a, b, c):
    return (a + b + c)/3

#Programa principal

a = int(input("Ingrese el primer numero entero: "))
b = int(input("Ingrese el segundo numero entero: "))
c = int(input("Ingrese el tercero numero entero: "))

promedio = calcular_promedio(a, b, c)

print(f"El promedio es: {promedio} ")