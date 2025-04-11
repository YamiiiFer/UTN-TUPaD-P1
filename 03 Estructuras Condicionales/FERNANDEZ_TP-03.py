#2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá
#mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el
#mensaje “Desaprobado”.
print("Ingrese su nota (recuerde que las notas pueden tener valores del 1 al 10)")
nota = int(input("Ingrese el valor de su NOTA: "))
if (nota >= 6):
    print("Aprobado")
else:
    print("Desaprobado")
    
    
#3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un
#número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso
#contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del
#operador de módulo (%) en Python para evaluar si un número es par o impar.
print("Número Pares")
num = int(input("Ingrese un número par: "))
if (num % 2 == 0):
    print( "Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")
    
    
#4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las siguientes categorías pertenece:
#● Niño/a: menor de 12 años.
#● Adolescente: mayor o igual que 12 años y menor que 18 años.
#● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
#● Adulto/a: mayor o igual que 30 años.
edad = int(input("Ingrese su edad: "))
if (edad < 12):
    print("Niño/a")
elif (edad >= 12 and edad < 18):
    print("Adolescente")   
elif ( edad >= 18 and edad < 30 ):
    print("Adulto/a joven")
else:
    print(" Adulto/a")
    

#5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres
#(incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en
#pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por
#pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso
#de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal
#como una lista o un string.
contraseña = (input("Ingrese una contaseña de entre 8 y 14 caracteres: "))
if (8 <= len(contraseña) <= 14):
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")


#6) Teniendo en cuenta lo antes mencionado, escribir un programa que tome la lista
#numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si
#hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.

from statistics import mode, median, mean
import random
numeros_aleatorios = [random.randint(1, 100) for i in range(10)]

media = mean(numeros_aleatorios)
moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)

print("Media: ", media)
print("Moda: ", moda)
print("Mediana: ", mediana)

if media > mediana:
    print("Sesgo positivo")
elif media < mediana:
    print("Sesgo negativo")
else:
    print("No hay sesgo")
    

#7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado
#termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por
#pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por pantalla.
frase = input("ingrese una frase o palabra: ")
vocales = "aeiouAEIOU"
if frase [-1] in vocales:
    resultado = frase + "!"
else:
    resultado = frase
print(resultado)



#8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3dependiendo de la opción que desee:
#1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
#2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
#3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
#El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el
#usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(),
#lower() y title() de Python para convertir entre mayúsculas y minúsculas.
nombre = input("Ingrese su nombre: ")
opcion = int(input("Ingrese la opción deseada (1, 2 o 3): "))

if opcion == 1:
    nombre = nombre.upper()
elif opcion == 2:
    nombre = nombre.lower()
elif opcion == 3:
    nombre = nombre.title()
else:
    nombre = "Opción invalida"
    
print("Su nombre modificado es: ", nombre)


#9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la
#magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado
#por pantalla:
#● Menor que 3: "Muy leve" (imperceptible).
#● Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
#● Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero
#generalmente no causa daños).
#● Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras
#débiles).
#● Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
#● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).
magnitud_terremoto = int(input("Ingrese la magnitud del terremoto"))
if magnitud_terremoto < 3:
    print("Muy leve (imperceptible).")
elif 3 <= magnitud_terremoto <=4:
    print("Leve(ligeramente perceptible).")
elif 4 <= magnitud_terremoto < 5:
    print("Moderado (sentido por personas, pero generalmente no causa daños)")
elif 5 <= magnitud_terremoto < 6:
    print("Fuerte (puede causar daños en estructuras débiles).")
elif 6 <= magnitud_terremoto < 7:
    print("Muy Fuerte (puede causar daños significativos).")
elif magnitud_terremoto >= 7:
    print("Extremo (puede causar graves daños a gran escala).")


from datetime import datetime
#entrada del usuario
hemisferio = input("¿En que hemisferio te encontrás? (N/S): ").strip().upper()
fecha_str = input("Ingresá la fecha en formato DD/MM (por ejemplo, 21/03): ")
# Convertimos la fecha a un objeto datetime (usamos 2024 como año ejemplo)
fecha = datetime.strptime(fecha_str + "/2024", "%d/%m/%Y")

# Extraemos mes y día
mes = fecha.month
dia = fecha.day

# Convertimos la fecha en formato MMDD para comparar fácilmente
mmdd = mes * 100 + dia

# Determinar la estación
if hemisferio == 'N':
    if mmdd >= 1221 or mmdd <= 320:
        estacion = "Invierno"
    elif 321 <= mmdd <= 620:
        estacion = "Primavera"
    elif 621 <= mmdd <= 920:
        estacion = "Verano"
    elif 921 <= mmdd <= 1220:
        estacion = "Otoño"
elif hemisferio == 'S':
    if mmdd >= 1221 or mmdd <= 320:
        estacion = "Verano"
    elif 321 <= mmdd <= 620:
        estacion = "Otoño"
    elif 621 <= mmdd <= 920:
        estacion = "Invierno"
    elif 921 <= mmdd <= 1220:
        estacion = "Primavera"
else:
    estacion = "Hemisferio no válido"

# Mostrar resultado
print(f"En el hemisferio {hemisferio}, el {fecha.strftime('%d/%m')} es {estacion}.")