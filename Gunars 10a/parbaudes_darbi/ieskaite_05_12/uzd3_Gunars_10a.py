vienmer = 'jā'
while vienmer == 'jā':
    Saraksts = []
    cik_skaitlus = int(input('Ievadiet skaitļu skaitu (nemazāk kā 3):  '))
    if cik_skaitlus >= 3:
        for i in range (1,cik_skaitlus+1,1):
            kuru_skaitli = 'ievadiet',i,'skaitli' #lai strādātu
            skaitlis = int(input(kuru_skaitli))     #šis
            Saraksts.append(skaitlis)
        print('Saraksts ar skaitļiem: ', Saraksts)
        Lielakais = max(Saraksts) #atrod lielāko
        print(f'Lielākais ievadītais skaitlis ir:{Lielakais}')
        exit()