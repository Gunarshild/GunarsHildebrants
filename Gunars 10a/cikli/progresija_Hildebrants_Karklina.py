print('Aritmētiskās progresijas elementu aprēķins')
PL=int(input('Ievadiet pirmo locekli! \n'))#pirmais loceklis
D=int(input('Ievadiet diferenci! \n'))#diferece
ES=int(input('ievadiet elementu skaitu! \n'))#Elementu skaits
P_L=ES*D+PL#pēdējais loceklis

x = 1

for i in range(PL,P_L,D):
    print(x,'.loceklis: ', i)
    x = x+1