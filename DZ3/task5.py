# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] Негафибоначчи
n = int(input('Введите число: '))

My_list=[0,1]
for i in range(n-1):
    f=My_list[i] + My_list[i+1]
    My_list.append(f)
My_list.insert(0,1)
for i in range(n-1):
    f=My_list[1]-My_list[0]
    My_list.insert(0,f)

print(f"Список чисел Фибоначчи для числа {n} равен {My_list}")