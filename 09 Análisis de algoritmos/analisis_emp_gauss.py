import time 
def sumGausN(n):                   # Define una función que recibe un número n
    start = time.time()           # Guarda el tiempo de inicio (antes de ejecutar el cálculo)
    res = n * (n + 1) / 2         # Aplica la fórmula de Gauss para sumar los primeros n números
    end = time.time()             # Guarda el tiempo de finalización (después de calcular)
    return res, (end - start) * 1000  # Devuelve el resultado y el tiempo total en milisegundos

print("n\t sumGausN(ms)")         # Imprime la cabecera de la tabla de resultados

for i in range(1, 9):                             # Repite el ciclo para valores de i desde 1 hasta 8 (inclusive)
    _, tiempo_total = sumGausN(10**i)             # Llama a la función con n = 10^i (10, 100, 1000, ..., 100000000)
    print(f"{10**i}\t {tiempo_total:.4f}")            # Imprime n y el tiempo que tardó en calcular la suma