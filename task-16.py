""" Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
*Пример:*
5
    1 2 3 4 5
    3
    -> 1   """

n = int(input("Ввод количества элементов в массиве: "))
a = list(map(int, input("Ввод самого массива(через пробел): ").split()))
x = int(input("Ввод числа, количество которого мы ищем: "))
count = 0  # счетчик
for i in range(n):
    if a[i] == x:
        count += 1  # если нашли число, увеличиваем счетчик
print(count)  # выводим количество найденных чисел x в массиве a