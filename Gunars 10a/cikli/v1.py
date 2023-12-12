#iztrukāt skaitļus 0,1,2,3,4,5
for i in range(6):#defaultā sāksies ar 0
    print(i)

print('----------------------------')

#izdrukāt 3,5,7
for i in range(3,8,2):
    print(i)

print('----------------------------')

n = int(input('ievadīt skaitli:'))
for i in range(1,11):
    print(n,'+',i,'=',n+i)

print('----------------')
#atrast skaitļu 2 un 4 dalītājus
#uz ekrāna parādīt tos, kas dalās ar 2, tos kas dalās gan ar 4,gan 2
#range 50

n = int(input('ievadīt skaitli no 1 līdz 50:'))
for i in range(2,5,2):
    print(n,'/',i,'=',round (n/i))
