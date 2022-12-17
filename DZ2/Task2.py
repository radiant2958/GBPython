#Задайте список из n чисел последовательности (1 + 1/n)^n, выведеите его на экран, а так же сумму элементов списка.
#Пример:
#Для n=4 -> [2, 2.25, 2.37, 2.44]
#Сумма 9.06

n=int(input("Введите число n: "))
my_list=[]
for i in range(1,n+1):
    b=(1+1/i)**i
    if b%2==0 or (b+1)%2==0:
        b=int(b)
        my_list.append(b)
    else:
        b=round(b,2)
        my_list.append(b)
print(my_list)

sum=0
for i in range(len(my_list)):
    sum=sum+my_list[i]
print(sum)
