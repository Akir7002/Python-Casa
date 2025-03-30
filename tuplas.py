# Ejercicio 1: Suma de elementos de una lista
def suma_lista(lista):
    total = 0
    for num in lista:
        total += num
    return total

# Ejemplo:
mi_lista = [1, 2, 3, 4, 5]
print("Ejercicio 1:", suma_lista(mi_lista))  # Salida: 15

# Ejercicio 2: Máximo y mínimo de una lista
def max_min(lista):
    if not lista:
        return None, None
    maximo = minimo = lista[0]
    for num in lista:
        if num > maximo:
            maximo = num
        if num < minimo:
            minimo = num
    return maximo, minimo

# Ejemplo:
print("Ejercicio 2:", max_min([5, 2, 9, 1, 7]))  # Salida: (9, 1)

# Ejercicio 3: Eliminar duplicados sin usar set()
def eliminar_duplicados(lista):
    lista_sin_duplicados = []
    for elemento in lista:
        if elemento not in lista_sin_duplicados:
            lista_sin_duplicados.append(elemento)
    return lista_sin_duplicados

# Ejemplo:
print("Ejercicio 3:", eliminar_duplicados([1, 2, 2, 3, 3, 3]))  # Salida: [1, 2, 3]

# Ejercicio 4: Invertir lista sin usar sort ni slices
def invertir_lista(lista):
    lista_invertida = []
    for i in range(len(lista)-1, -1, -1):
        lista_invertida.append(lista[i])
    return lista_invertida

# Ejemplo:
print("Ejercicio 4:", invertir_lista([1, 2, 3, 4]))  # Salida: [4, 3, 2, 1]

# Ejercicio 5: Verificar si un elemento está en la lista
def existe_elemento(lista, elemento):
    for item in lista:
        if item == elemento:
            return True
    return False

# Ejemplo:
print("Ejercicio 5:", existe_elemento(["a", "b", "c"], "b"))  # Salida: True

# Ejercicio 6: Contar ocurrencias de un valor
def contar_ocurrencias(lista, valor):
    contador = 0
    for elemento in lista:
        if elemento == valor:
            contador += 1
    return contador

# Ejemplo:
print("Ejercicio 6:", contar_ocurrencias([1, 2, 2, 3, 2], 2))  # Salida: 3

# Ejercicio 7: Ordenar lista sin usar sort()
def ordenar_lista(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista

# Ejemplo:
print("Ejercicio 7:", ordenar_lista([3, 1, 4, 1, 5]))  # Salida: [1, 1, 3, 4, 5]