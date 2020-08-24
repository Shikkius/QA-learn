#Напишите программу, которая сравнивает количество перестановок
#при сортировке одного и того же списка методом пузырька и методом вставок

#заводим псевдорандомный список
from random import randint
N = 10
A = []
for i in range(N):
    A.append(randint(1, 99))
print(f'Изначальный список: {A}')

i = 0
countBubble = 0
while i < N-1:
    j = 0
    countBubble += 1
    while j < N-i-1:
        if A[j] > A[j+1]:
            A[j], A[j+1] = A[j+1], A[j]
        j += 1
    i += 1
print(f'Сортировка пузырьком: {A}')

countInsertinon = 0
def insertion(A):
    for i in range(1, len(A)):
        b = A[i]
        j = i - 1
        global countInsertinon
        while (j >= 0) and (b < A[j]):
            A[j+1] = A[j]
            j -= 1
        A[j+1] = b
        countInsertinon += 1
    return A

insertion(A)
print(f'Сортировка вставками: {A}')
print(f'Количество перестановок при пузырьковой сотрировке: {countBubble}')
print(f'Количество перестановок при сортировке вставками: {countInsertinon}')
print(f'Разница в перестановках: {(countBubble) - (countInsertinon)}')