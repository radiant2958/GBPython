# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит заданное количество конфет. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход.

from random import randint
player1=input('Введите имя первого игрока: ')
player2=input('Введите имя второго игрока: ')
quantity_candies=int(input('Введите количество конфет лежащих на столе: '))

queue=randint(1,2)
if queue==1:
    print(f'первый ходит {player1}')
else:
    print(f"первый ходит {player2}")

def take_candy(player):
    x=int(input(f'{player} введите колличество конфет которое возьмете от 1 до 28: '))
    if x<1 or x>28:
        x=int(input('нарушение условия игры,введите корректное колличество конфет от 1 до 28: '))
    
    return x
    
count1=0
count2=0

while quantity_candies>28:
    if queue==1:
        candy=take_candy(player1)
        count1+=candy
        quantity_candies-=candy
        queue=False
        print(f'{player1} взял {candy} конфет, осталось на столе {quantity_candies} конфет')
    else:
        candy=take_candy(player2)
        count2+=candy
        quantity_candies-=candy
        queue=True
        print(f'{player2} взял {candy} конфет, осталось на столе {quantity_candies} конфет')

if queue==1:
    print(f"выйграл первый игрок {player1}")
else:
    print(f"выйграл второй игрок {player2}")
