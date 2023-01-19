# Создайте программу для игры в 'Крестики-нолики'
from random import randint

player1 = input('Введите имя первого игрока: ')
player2 = input('Введите имя второго игрока: ')

queue=randint(1,2)
if queue==1:
    print(f'первый ходит {player1}')
else:
    print(f"первый ходит {player2}")

field=[0,1,2,3,4,5,6,7,8]

def field_pr(field):
    print(field[:3],end = '\n')

    print(field[3:6],end='\n')

    print(field[6:9])

field_pr(field)

game=True

def victory(field):
    game=True
    if field[0]=='X' and field[1]=="X" and field[2]=="X":
        game=False
        
    elif field[0]=='O' and field[1]=="O" and field[2]=="O":
        game=False
        
    elif field[3]=='X' and field[4]=="X" and field[5]=="X":
        game=False
        
    elif field[3]=='O' and field[4]=="O" and field[5]=="O":
        game=False
        
    elif field[6]=='X' and field[7]=="X" and field[8]=="X":
        game=False
        
    elif field[6]=='O' and field[7]=="O" and field[8]=="O":
        game=False
        
    elif field[0]=='X' and field[3]=="X" and field[6]=="X":
        game=False
        
    elif field[0]=='O' and field[3]=="O" and field[6]=="O":
        game=False
        
    elif field[1]=='X' and field[4]=="X" and field[7]=="X":
        game=False
    
    elif field[1]=='O' and field[4]=="O" and field[7]=="O":
        game=False
        
    elif field[2]=='X' and field[5]=="X" and field[8]=="X":
        game=False
        
    elif field[2]=='O' and field[5]=="O" and field[8]=="O":
        game=False
        
    elif field[0]=='X' and field[4]=="X" and field[8]=="X":
        game=False
        
    elif field[0]=='O' and field[4]=="O" and field[8]=="O":
        game=False
        
    elif field[2]=='X' and field[4]=="X" and field[6]=="X":
        game=False
        
    elif field[2]=='O' and field[4]=="O" and field[6]=="O":
        game=False
    return game
    
i=1
while game==True and i<10:
    if queue==1:
        step=int(input('Введите номер ячейки для хода от 0 до 8: '))
        if field[step]=='X' or field[step]=='O':
            step=int(input('клетка занята, введите другой номер ячейки: '))
        else:
            field[step]="X"
            m=victory(field)
            if m==False:
                game=False
                
            else:
               field_pr(field)
               i+=1
               queue=False
        
    else:
        step=int(input('Введите номер ячейки для хода от 0 до 8: '))
        if field[step]=='X' or field[step]=='O':
            step=int(input('клетка занята, введите другой номер ячейки: '))
        else:
            field[step]="O"
            m=victory(field)
            if m==False:
                game=False
            else:
               field_pr(field)
               i+=1
               queue=True


if i==9:
    print('Победила дружба!')
    field_pr(field)
elif queue==1:
    print(f"выйграл первый игрок {player1}")
    field_pr(field)
else:
    print(f"выйграл второй игрок {player2}")
    field_pr(field)




