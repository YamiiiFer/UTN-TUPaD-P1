#1) Crear una lista con los números del 1 al 100 que sean múltiplos de 4. Utilizar la función range

#creeamos la variable numeros que va a ser igual a la lista en el rango de 4 a 100 con incremento de 4

numeros = list(range(4, 100, 4))
print(numeros)

#2) Crear una lista con cinco elementos (colocar los elementos que más te gusten) y mostrar el
#penúltimo. ¡Puedes hacerlo como se muestra en los videos o bien investigar cómo funciona el
#indexing con números negativos!

lista = ["a", "b", "c","d", "e"]

print(lista[3]) #print(lista[3])

#3) Crear una lista vacía, agregar tres palabras con append e imprimir la lista resultante por
#pantalla. Pista: para crear una lista vacía debes colocar los corchetes sin nada en su interior. Por
#ejemplo:
#lista_vacia = []
#creamo una lista vacia llamada palabras
palabras = []
#usamos append para agregar elementos, en este caso palabras
palabras.append("Yami")
palabras.append("Lore")
palabras.append("Abi")
#imprimimos la nueva lista :)
print(palabras)

#4) Reemplazar el segundo y último valor de la lista “animales” con las palabras “loro” y “oso”,
#respectivamente. Imprimir la lista resultante por pantalla. ¡Puedes hacerlo como se muestra
#en los videos o bien investigar cómo funciona el indexing con números negativos!
#animales = ["perro", "gato", "conejo", "pez"]

animales = ["perro", "gato", "conejo", "pez"]
#cambiio el elmento -2 que es conejo por loro
animales[-2] = "loro"
#cambio el elemento -1 que es pez por oso
animales[-1] = "oso"
#imprimo la lista modificada
print(animales)

#5) Analizar el siguiente programa y explicar con tus palabras qué es lo que realiza.
 #tenemos una lista con los siguiente numeros
 
numeros = [8, 15, 3, 22, 7]

#remove(max()) es para eliminar el numero mas grande de la lista

numeros.remove(max(numeros))
#nos muestra la lista sin el 22, que es el numero mas grande
print(numeros)
 
 
#6) Crear una lista con números del 10 al 30 (incluído), haciendo saltos de 5 en 5 y mostrar por
#pantalla los dos primeros.
#creamos una lista con rango del 10 al 30 incluido con saltos de 5 en 5
lista = list(range(10, 31, 5))

#mostramos por pantalla el elemento 0 y uno
print(lista[0], lista[1])

#7) Reemplazar los dos valores centrales (índices 1 y 2) de la lista “autos” por dos nuevos valores cualesquiera.
#autos = ["sedan", "polo", "suran", "gol"]

autos = ["sedan", "polo", "suran", "gol"]

#remplazamos los valore centrale, polo y suran 

autos[1] = "manzana"

autos[2] = "pera"

print(autos)

#8) Crear una lista vacía llamada "dobles" y agregar el doble de 5, 10 y 15 usando append
#directamente. Imprimir la lista resultante por pantalla.

#creamos la lista vacia
dobles = []
#usamos la fincion append y dentro de la funcion realizamos la operacion aritmetica necesaria
dobles.append(5 * 2)
dobles.append(10 * 2)
dobles.append(15 * 2)

print(dobles)

#9) Dada la lista “compras”, cuyos elementos representan los productos comprados por diferentes clientes:
#compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]
#a) Agregar "jugo" a la lista del tercer cliente usando append.
#b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente.
#c) Eliminar "pan" de la lista del primer cliente.
#d) Imprimir la lista resultante por pantalla

# Lista inicial
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]

# a) Agregar "jugo" al tercer cliente (índice 2)
compras[2].append("jugo")

# b) Reemplazar "fideos" por "tallarines" en el segundo cliente (índice 1)
indice_fideos = compras[1].index("fideos")
compras[1][indice_fideos] = "tallarines"

# c) Eliminar "pan" del primer cliente (índice 0)
compras[0].remove("pan")

# d) Imprimir la lista resultante
print(compras)

#10) Elaborar una lista anidada llamada “lista_anidada” que contenga los siguientes elementos:
#● Posición lista_anidada[0]: 15
#● Posición lista_anidada[1]: True
#● Posición lista_anidada[2][0]: 25.5
#● Posición lista_anidada[2][1]: 57.9
#● Posición lista_anidada[2][2]: 30.6
#● Posición lista_anidada[3]: False
#Imprimir la lista resultante por pantalla.

lista_anidada = [
     15,                    # lista_anidada[0]
    True,                  # lista_anidada[1]
    [25.5, 57.9, 30.6],    # lista_anidada[2][0], [2][1], [2][2]
    False                  # lista_anidada[3]
]

print(lista_anidada)