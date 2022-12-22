#Напишите программу, которая будет преобразовывать десятичное число в двоичное.
#Пример:
#45 -> 101101
#3 -> 11
#2 -> 10
number=int(input('Введите число:'))
my_list=[]
number1=number
while number1!=1:
    b=number1%2
    my_list.append(b)
    number1=int(number1/2)
my_list.append(1)
my_list.reverse()
print(f"Десятичное число {number} в двоичной системе равно ", *my_list, sep ='')