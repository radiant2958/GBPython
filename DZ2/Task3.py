#Реализуйте алгоритм перемешивания списка. НЕ ИСПОЛЬЗОВАТЬ ВСТРОЕННЫЕ БИБЛИОТЕКИ SHUFFLE, 
#максимум использование библиотеки Random для и получения случайного int
import random
my_list=[]
for i in range(10):
    a=random.randint(0,100)
    my_list.append(a)
print(my_list)
tmp=0
new_my_list=[]
for i in range(len(my_list)-1,0,-1):
    new_my_list.append(my_list[i])

print(new_my_list)  
    



