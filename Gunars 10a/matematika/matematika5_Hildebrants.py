import math

print("Programmu izstrādāja: Gunārs Hildebrants" )
print("Laukuma aprēķins ģeometriskām figūrām\n      ****")

malaA = int(input('Ievadiet malas A garumu\n '))
print('malas A garums: ''%.1f'%malaA)       #Ievada malas a garumu 
print('****')

malaB = int(input('Ievadiet malas B garumu\n'))
print('malas B garums: '"%.1f"%malaB)       #Ievada malas b garumu 
print('****')

augstums = int(input('Ievadiet augstumu\n'))
print('augstuma garums: '"%.1f"%augstums)  #Ievada augstuma garumu 

s = malaA*augstums/2
print('Laukums trijstūrim: '"%.1f"%s)

s = (malaA+malaB)/2*augstums
print('laukums trapecei: '"%.1f"%s)

s = malaA*augstums
print('laukums paralelogramam: '"%.1f"%s)
print("****\nPaldies!")

