## @file fibonacci.py
# @brief Este archivo contiene una implementación recursiva de la secuencia de Fibonacci.

def fibonacci(n):
    """
    @brief Calcula el n-ésimo número de la secuencia de Fibonacci de forma recursiva.

    La secuencia de Fibonacci es una serie de números donde cada número es la suma de los dos anteriores.
    Esta implementación utiliza recursión para calcular el valor.

    @param n El índice del número en la secuencia de Fibonacci (debe ser un entero no negativo).
    @return El n-ésimo número en la secuencia de Fibonacci.

    @note Esta implementación es simple pero ineficiente para valores grandes de `n` debido a la recursión múltiple.
    Para valores grandes, se recomienda usar una implementación iterativa o con memoización.

    @code
    # Ejemplo de uso:
    for i in range(25):
        print(fibonacci(i), end=" ")
    # Salida: 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181 6765 10946 17711 28657 46368
    @endcode
    """
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


# Ejemplo de uso
if __name__ == "__main__":
    """
    @brief Ejemplo de uso de la función fibonacci.
    
    Imprime los primeros 25 números de la secuencia de Fibonacci.
    """
    for i in range(25):
        print(fibonacci(i), end=" ")