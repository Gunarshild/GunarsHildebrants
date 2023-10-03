print('šoferi atsakās gaidīt ilgāk par 5 min')
eiro = 'eiro'
skaits = int(input('cik pasažieri brauks? (cipars) ')) #pasažieru skaits
if skaits == 1 or skaits == 2 or skaits == 3:
    vaiirstacija = (input('vai ir taksometri stacijā? (j/n) '))#vai ir taksometri stacijā
    if vaiirstacija == 'j':
        pulkstens = int(input('cik ir pulkstens? (vesalas stundas) '))#cik ir pulkstens
        if pulkstens >= 21 and pulkstens <=24 or pulkstens < 6:
            laiks = int(input('cik ilgi bus jāgaida? (min) '))#cik ilgi bus jāgaida
            if laiks > 5:#īpašība
                print('šoferis atsakās vest')
            else:
                distance = int(input('cik tālu būs jābrauc? (km) '))#cik tālu būs jābrauc
                cena = (0.77*distance+2,eiro)
                print('0.77 eiro*',distance,'+',laiks,'*0.15 eiro + 2 =',cena)
        elif pulkstens < 21 and pulkstens > 6:
            laiks = int(input('cik ilgi bus jāgaida? (min) '))#cik ilgi bus jāgaida
            if laiks > 5:#īpašība
                print('šoferis atsakās vest')
            else:
                distance = int(input('cik tālu būs jābrauc? (km) '))#cik tālu būs jābrauc
                cena = (0.37*distance+2,eiro)
                print('0.37 eiro*',distance,'+',laiks,'*0.15 eiro + 2 =',cena)
        else:
         print('ievadi pareizus datus.')
    elif vaiirstacija == 'n':
        pulkstens = int(input('cik ir pulkstens? (vesalas stundas) '))#cik ir pulkstens
        if pulkstens >= 21 and pulkstens <=24 or pulkstens < 6:
            laiks = int(input('cik ilgi bus jāgaida? (min) '))#cik ilgi bus jāgaida
            if laiks > 5:#īpašība
                print('šoferis atsakās vest')
            else:
                distance = int(input('cik tālu būs jābrauc? (km) '))#cik tālu būs jābrauc
                cena = (0.77*distance+2,eiro)
                print('0.37 eiro*',distance,'+',laiks,'*0.15 eiro + 2 =',cena)
            distance = int(input('cik tālu būs jābrauc? (km) '))#cik tālu būs jābrauc
            cena = (0.77*distance+laiks*0.15+2+2.5,eiro)
            print('0.77 eiro*',distance,'+',laiks,'*0.15 eiro + 2 + 2.50 =',cena)
        elif pulkstens < 21 and pulkstens > 6:
            laiks = int(input('cik ilgi bus jāgaida? (min) '))#cik ilgi bus jāgaida
            if laiks > 5:#īpašība
                print('šoferis atsakās vest')
            else:
                distance = int(input('cik tālu būs jābrauc? (km) '))#cik tālu būs jābrauc
                cena = (0.37*distance+2,eiro)
                print('0.37 eiro*',distance,'+',laiks,'*0.15 eiro + 2 =',cena)
                distance = int(input('cik tālu būs jābrauc? (km) '))#cik tālu būs jābrauc
            cena = (0.37*distance+laiks*0.15+2+2.5,eiro)#cena
            print('0.37 eiro*',distance,'+',laiks,'*0.15 eiro + 2 + 2.50 =',cena)
        else:
             print('ievadi pareizus datus.')
    else:
         print('ievadi pareizus datus.')
else:
    print('nevar vest šādu skaitu cilvēku.')