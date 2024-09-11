
def insertion_sort(arr):
    #Primer bucle, se repite una vez por cada elemento del dataset-1
    for i in range(1, len(arr)):
        #Curr == elemento a ordenar
        curr = arr[i]
        j = i - 1
        #Segundo bucle, se repite i veces, i == cantidad de elementos ya ordenados
        #Compara elemento a ordenar con elemento aen j
        while j >= 0 and curr < arr[j]:
            #Intercambia posiciones
            arr[j + 1] = arr[j]
            j -= 1
        #
        arr[j + 1] = curr

    return arr

def mergeSort(arr):
    #Para arreglos con 1 o 0 elementos:
    if len(arr) <=1:
        return arr
    #Toma punto medio
    i = len(arr)/2
    #Ejecuta recursivamente la funcion en cada mitad del arreglo
    izq = mergeSort(arr[:i])
    der = mergeSort(arr[i:])
    #
    return merge(izq, der)

def merge(izquierda, derecha):
        union = []
        a, b = 0
        while a < len(izquierda) and b < len(derecha):
            if izquierda[a] < derecha[b]:
                union.append(izquierda[a])
                a+=1
            else:
                union.append(derecha[b])
                b+=1
        if a > len(izquierda):
            union.extend(izquierda[a:])
        else:
            union.extend(derecha[b:])
        return union
    
def quicksort(arr):
    # Para arreglos con 1 o 0 elementos
    if len(arr) <= 1:
        return arr

    #Pivote 
    pivote = arr[0]
    menor_que = []
    mayor_que = []
    
    for elem in arr[1:]:
        #Si elemento es menor va a una lista, si es mayor a la otra.
        if elem < pivote:
            menor_que.append(elem)
        else:
            mayor_que.append(elem)
    #Recurisividad para ordenar subarreglos
    return quicksort(menor_que) + pivote + quicksort(mayor_que)
