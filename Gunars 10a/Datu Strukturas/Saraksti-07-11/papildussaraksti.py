#Piemērs sarakstam ar dažādiem datu tipiem
mixed_list = ['suns',7.25,8,True]
print(mixed_list[2])

print('---------------------------------------------------')

skaitli = [1,2,3,4,5,6,7,3,4]
appgriezts = list(reversed(skaitli))
print(appgriezts)

print('---------------------------------------------------')

#Filtrēt tikai pāra skaitļus
Para_skaitli = [num for num in skaitli if num%2 == 0]
print(Para_skaitli)

print('---------------------------------------------------')

videjais = sum(skaitli)/len(skaitli)
print(f'Vidējais skaitlis: {videjais}')

print('---------------------------------------------------')

#atrast lielāko un mazāko skaitli, paraādīt uz ekrāna
Lielakais = max(skaitli)
mazakais = min(skaitli)
print(f'Mazākais skaitlis ir:{mazakais}')
print(f'Lielākais skaitlis ir:{Lielakais}')

print('---------------------------------------------------')

augli = ['abols','citrons','apeklsins','bumbieris','ananass']
#atrast vardus, kas sakas ar konkoretu burtu
varda_sakums = [vards for vards in augli if vards.startswith('a')]
print(f'Vārdi kas sākas ar "a":{varda_sakums}')