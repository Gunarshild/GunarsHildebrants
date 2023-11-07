

saraksts1 = []
saraksts2 = []
#pirmais saraksts
print('ievadi 1. sraksta garumu:  ')
garums = int(input())#lietotājs pats ievada 


for i in range(garums):
    lieta1 = input('Ievadat saraksta elementu: ')
    saraksts1.append(lieta1)
print('Pirmā saraksta elementi:',saraksts1)

print('--------------------------------------------')

print('ievadi 2. sraksta garumu:  ')
garums2 = int(input())#lietotājs pats ievada 

for j in range(garums):
    lieta2 = input('Ievadat saraksta elementu: ')
    saraksts2.append(lieta2)
print('Otrā saraksta elementi:',saraksts2)


print('--------------------------------------------')
saraksts3 = saraksts1 + saraksts2

print(saraksts3)