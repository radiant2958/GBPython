#Напишите программу, которая найдёт произведение пар чисел списка. 
#Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#Пример:
#[2, 3, 4, 5, 6] => [12, 15, 16];
#[2, 3, 5, 6] => [12, 15]
import random

n = int(input('задайте длину списка:'))
my_list = []
for i in range(n):
    a = random.randint(0, 10)
    my_list.append(a)
print(my_list)
l=0
if n%2==0:
    l=(n/2)
else:
    l=n/2
    l=int(l)+1

my_list2=[]
for i in range(int(l)):
    p=my_list[i]*my_list[len(my_list)-i-1]
    my_list2.append(p)
print(my_list2)
