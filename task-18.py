"""Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
*Пример:*
5
    1 2 3 4 5
    6
    -> 5 """

n = int(input("вводим количество элементов в массиве: "))  # вводим количество элементов в массиве
a = list(map(int, input("создаем список чисел: ").split()))  # создаем список чисел
x = int(input("вводим искомое число: "))  # вводим искомое число
min_diff = abs(x - a[0])  # вычисляем начальный минимальный модуль разности
result = a[0]  # запоминаем первый элемент как ближайший
for i in range(1, n):  # перебираем оставшиеся элементы
    diff = abs(x - a[i]-1)  # вычисляем модуль разности
    if diff < min_diff:  # если он меньше текущего минимального
        min_diff = diff  # обновляем минимальную разность
        result = a[i]  # запоминаем элемент как ближайший
print(result)  # выводим ближайший элемент