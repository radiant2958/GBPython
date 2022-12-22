#Задайте список из вещественных чисел. Напишите программу, 
#которая найдёт разницу между максимальным и минимальным значением дробной части элементов, отличной от 0.
#Пример:
#[1.1, 1.2, 3.1, 5, 10.01] => 0.19
import random
n = int(input('задайте длину списка:'))
my_list = []
for i in range(n):
    a = random.uniform(1,10)
    my_list.append(round(a,2))
print(my_list)
max=0
for i in range(len(my_list)):
    d=my_list[i]-int(my_list[i])
    if d>max:
        max=round(d,2) 
print(f"максимальное значение дробной части элементов ровна {max}")
min=my_list[0]-int(my_list[0])
for i in range(1,len(my_list)):
    d=my_list[i]-int(my_list[i])
    if d<min:
        min=round(d,2) 
print(f"минимальное значение дробной части элементов ровна {min}")

print(f"Разница между максимальным и минимальным значением дробной части равна: {round(max-min,2)}")
