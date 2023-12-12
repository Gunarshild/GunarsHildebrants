saraksts = [2,4,6,2,7,2,7,3,8,1]
print('Saraksts:  ',saraksts)
para_skaitli = [num for num in saraksts if num%2 == 0] #atrod para skaitļus
print('Pāra skaitļu skaits:  ',len(para_skaitli))  #saskaita para skaitļus
nepara_skaitli = [num for num in saraksts if num%2 != 0] #atrod nepara skaitļus
print('Nepāra skaitļu skaits:  ',len(nepara_skaitli))  #saskaita nepara skaitļus
