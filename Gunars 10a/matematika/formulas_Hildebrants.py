import math   #lai var izmantot
import random

radiuss = int(input('Ievadiet rinķa līnijas rādiusu:'))
print(radiuss) #ievada radiusu

PI = 3.1415
garums = 2*PI*radiuss       #aprēķini
laukums = math.pow(radiuss,2)*PI  

print('Rinķa līnijas garums:',"%.2f"%garums)    #parāda aprēķinus rinķa līnijai
print('Rinķa līnijas Laukums:', "%.2f"%laukums)

katete1 = int(input('Ievadiet taisnlenķa trijstūra pirmās katetes garumu:'))
print(katete1)
katete2 = int(input('Ievadiet taisnlenķa trijstūra otrās katetes garumu:'))
print(katete2)
h = math.sqrt(math.pow(katete1,2)+math.pow(katete2,2))
print('Taisnlenķa trijstūra hipotenūzas garums:', "%.2f"%h)    #hipetonūzas aprēķins

skaitlis = random.random() #izvēlas nejaušu skaitli
print('Gadījuma skaitlis no 0 - 1:',skaitlis )