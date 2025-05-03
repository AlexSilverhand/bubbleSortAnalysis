# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 08:15:22 2024

@author: diego
"""

import matplotlib.pyplot as plt
import random

# Bubble Sort


def bubbleSort(arr):
    operations = 2  # Constante inicial
    n = len(arr)
    for i in range(n):
        for j in range(n-1): # 1
            if arr[j] > arr[j+1]: # 4
                temp = arr[j] # 2
                arr[j] = arr[j+1] # 4
                arr[j+1] = temp # 3
                operations = 16 * n**2 - 10 * n
    return operations

# Optimized Bubble Sort
def optimizedBubbleSort(arr):
    operations = 2  # Constante inicial
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(n-1):  # 1
            if arr[j] > arr[j+1]:  # 4
                temp = arr[j]  # 2
                arr[j] = arr[j+1]  # 4
                arr[j+1] = temp  # 3
                swapped = True # 1
                operations += 18
        if not swapped:
            break
        operations += (n-1) * 4
    return operations

# Variables para graficar
sizes = []  # Guarda tamaños de los arreglos
operationsBubble = []  # Guarda número de operaciones de Bubble sort
operationsOptimized = []  # Guarda número de operaciones de Bubble sort mejorado

# Probar diferentes tamaños de arreglo desde 100 has 1000, con incrementos de 100
for size in range(100, 1001, 100):
    arr = [random.randint(0, 10000) for _ in range(size)]

    arr1 = arr.copy()
    arr2 = arr.copy()

    # Medir operaciones para Bubble Sort
    opsBubble = bubbleSort(arr1)
    # print("Bubble Sort: ",opsBubble)

    # Medir operaciones para Optimized Bubble Sort
    opsOptimized = optimizedBubbleSort(arr2)
    # print("Bubble Sort Mejorado: ",opsOptimized)

    # Guardar resultados
    sizes.append(size)
    operationsBubble.append(opsBubble)
    operationsOptimized.append(opsOptimized)

# Graficar resultados
plt.figure(figsize=(10, 6))
plt.plot(sizes, operationsBubble, label='Bubble Sort', marker='o')
plt.plot(sizes, operationsOptimized, label='Bubble Sort Mejorado', marker='x')
plt.xlabel('Tamaño del arreglo')
plt.ylabel('Número de operaciones')
plt.title('Número de Operaciones vs Tamaño del Arreglo')
plt.legend()
plt.grid()
plt.show()
