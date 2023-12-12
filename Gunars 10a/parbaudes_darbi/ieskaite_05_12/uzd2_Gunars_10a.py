from math import * 
tempreturas = {
'1.decembris' : -3,
'2.decembris' : -5,
'3.decembris' : -7,
'4.decembris' : -10,
'5.decembris' : -6,
'6.decembris' : -8,
'7.decembris' : -2
}

kurs_datums = input("Ievadiet datumu (piemēram,'1.decembris'): ")
if kurs_datums in tempreturas:
    print('šajā dienā tempretūra Celsija skalā ir ',tempreturas[kurs_datums],'grādi') #šajā dienā jo man nestrādāja
else: #ja ir nepareizs
    print('Nepareiza atslēga. Lūdzu , ievadiet datumu no 1. līdz 7. decembrim')
    kurs_datums = input("Ievadiet datumu (piemēram,'1.decembris'): ")
    if kurs_datums in tempreturas:
         print('šajā dienā tempretūra Celsija skalā ir ',tempreturas[kurs_datums],'grādi')
    else: 
        print('Nepareiza atslēga. Lūdzu , ievadiet datumu no 1. līdz 7. decembrim')
        kurs_datums = input("Ievadiet datumu (piemēram,'1.decembris'): ")
        if kurs_datums in tempreturas:
             print('šajā dienā tempretūra Celsija skalā ir ',tempreturas[kurs_datums],'grādi')
        else:
            print('Nepareiza atslēga. Lūdzu , ievadiet datumu no 1. līdz 7. decembrim')
            kurs_datums = input("Ievadiet datumu (piemēram,'1.decembris'): ")
            if kurs_datums in tempreturas:
                 print('šajā dienā tempretūra Celsija skalā ir ',tempreturas[kurs_datums],'grādi')
            else:
                exit()