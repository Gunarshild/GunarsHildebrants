derigais_litotajv = 'skolens' #lietotājvārds
deriga_parole = 'zupas' #parole
iznakums = 0 
for meginajumi in range(4,-1,-1): #Cik mēģinājumi (5)

    lietotajv = input('lūdzu, ievadiet savu lietotājvārdu: ')
    parole = input('lūdzu, ievadiet savu paroli: ')
    parolesgarums = len(parole)# pārbauda cik gara ir parole

    if lietotajv == derigais_litotajv and parole == deriga_parole:  #pārbauda vai der litotājvārds un parole
        print('Pieslēgšanās veiksmīga.')
        skaitlis1 = int(input('Ievadiet 1. vesalo skaitli: (ja grib beigt tad raksti 0) '))
        skaitlis2 = int(input('Ievadiet 2. vesalo skaitli: (ja grib beigt tad raksti 0) '))
        if skaitlis1 == 0 or skaitlis2 == 0: #pārbauda vai grib lai programma beidzas 0 ir jo man nepārveidujās uz str mainīgo un atpakaļ uz int mainīgo
            print('Programmas beigas!')
            exit()
        elif skaitlis2 < 0 or skaitlis1 < 0:#pārbauda vai ir pozitīvs skaitlis
            print('Nedrīkst būt negatīvs skaitlis!')
            exit()
        elif  skaitlis1 > skaitlis2:#pārbauda vai 1. skaitlis ir lieklāks par 2. skaitli
            print('summa ir 0')
        else:
            for i in range(skaitlis1,skaitlis2+1):#aprēķina
                iznakums+= i
            print('Veselu secīgi pieaugušu skaitļu no ',skaitlis1,' līdz ',skaitlis2,' summa ir ',iznakums,'!')
            exit()
    elif parolesgarums > 5:
        print('Parolei ir jābūt 5 rakstzīmes garai!')
        print('Ir atlikuši ',meginajumi,' mēģinājumi!')#viss sākas no jauna
    else:
        print('Ir atlikuši ',meginajumi,' mēģinājumi!')#viss sākas no jauna