#Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
#Пример:
#6782 -> 23
#0,56 -> 11
number=float(input("Введите число:  "))
sum=0
if number-int(number)<0:
    while number >0:
        sum=sum+number%10
        number=number//10
else:
    number=str(number).replace('.',"")
    while int(number) >0:
        sum=sum+int(number)%10
        number=int(number)//10

print(sum)


