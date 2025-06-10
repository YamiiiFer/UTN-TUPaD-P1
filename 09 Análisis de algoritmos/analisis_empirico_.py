import time      # Se importa el módulo time para medir el tiempo de ejecución

def sumN(n):
    start = time.time()     # Se guarda el tiempo de inicio
    res = 0     # Se inicializa la variable acumuladora
    for i in range(1, n + 1):    # Se recorre desde 1 hasta n (inclusive)
        res += i    # Se suma cada número al acumulador
    end = time.time()    # Se guarda el tiempo de finalización
    return res, (end - start) * 1000  # Se retorna la suma y el tiempo en milisegundos

print("n\t sumN(ms)")   # Encabezado de la tabla que se imprimirá
for i in range(1, 9):    # Se prueba con tamaños de entrada 10^1 hasta 10^8
    _, tiempo_total = sumN(10**i)   # Se llama a sumN con el tamaño actual y se guarda solo el tiempo
    print(f"{10**i}\t {tiempo_total:.4f}")  # Se imprime el tamaño de entrada y el tiempo en ms, con 4 decimales