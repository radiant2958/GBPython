# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
# aaaaabbbcccc -> 5a3b4c
# 5a3b4c -> aaaaabbbcccc
data=open('RLE.txt','r')
data=data.read()
print(data)
def encodr(data:str)->str:
    new_data=''
    count=1

    for i in range(len(data)-1):
        if data[i]==data[i+1]:
            count+=1
        else:
            new_data+=str(count)+data[i]
            count=1


    if count>1:
        new_data+=str(count)+data[-1]
        
    
    return new_data

f=encodr(data)
print(f)

def write_file(file):
   with open('RLE3.txt', 'w') as date:
      date.write(file)

# write_file(f)

def decodr(data):
    new_data=''
    for i in range(len(data)):
        if data[i].isdigit():
            new_data=new_data+int(data[i])*data[i+1]
    return new_data

print(decodr(f))
d=decodr(f)
write_file(d)