#Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка,
# стоящих на позиции с нечетным индексом.
#Пример:
#[2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
import random

n = int(input('задайте длину списка:'))
my_list = []
for i in range(n):
    a = random.randint(0, 10)
    my_list.append(a)
print(my_list)
sum_el = 0
for i in range(len(my_list)):
    if i % 2 != 0:
        sum_el += my_list[i]

print(sum_el)
