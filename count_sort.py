#Напишите программу, которая сравнивает количество перестановок
#при сортировке одного и того же списка методом пузырька и методом вставок

#заводим псевдорандомный список
from random import randint

CBL = 0
def bubble_sort(A):
    global CBL
    for i in range(N-1):
        for j in range(N-i-1):
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]
                CBL += 1
    return A

N = 10
A = []
for i in range(N):
    A.append(randint(1, 99))
print(f'Изначальный список: {A}')

CINS = 0
def insertion(A):
    for i in range(1, len(A)):
        b = A[i]
        j = i - 1
        global CINS
        while (j >= 0) and (b < A[j]):
            A[j+1] = A[j]
            j -= 1
        A[j+1] = b
        CINS += 1
    return A

bubble_sort(A)
insertion(A)
print(f'Сортировка пузырьком: {A}')
print(f'Сортировка вставками: {A}')
print(f'Количество перестановок при пузырьковой сотрировке: {CBL}')
print(f'Количество перестановок при сортировке вставками: {CINS}')
print(f'Разница в перестановках: {(CBL) - (CINS)}')