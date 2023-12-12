while True:

    print('Rimi ir 30% atlaide!')
    print('Maxima ir 40% atlaide ja ir karte!')
    print('Top ir 20% atlaide un 50 % atlaide ja ir karte1!')
    print('Lats ir 30% atlaide ja pērk 3 preces un vairā!')
    print('Elvi katra otrā prece ir par brīvu!')




    Kura_veikala = str(input('kurā veikalā jūs iepirksities? '))
    if Kura_veikala == 'Rimi':
        prece = input('kādu preci jūs pirksiet? ') 
        cik_prece = int(input('Cik šo preci jūs pirksiet?(paciņu skaits)')) 
        prece_cena = float(input('kāda cena ir precei? (eiro) '))
        viss_nopirkts = input('Vai nopirkts viss kas sarakstā (j/n)? ') 
        cena = cik_prece*prece_cena/100*70

    elif Kura_veikala == 'Maxima':
        prece = input('kādu preci jūs pirksiet? ') 
        cik_prece = int(input('Cik šo preci jūs pirksiet?(paciņu skaits)')) 
        prece_cena = float(input('kāda cena ir precei? (eiro) '))
        viss_nopirkts = input('Vai nopirkts viss kas sarakstā (j/n)? ') 
        vai_ir_karte = str(input('vai jums ir biedra karte? (j/n)'))
        if vai_ir_karte == 'j':
            cena = cik_prece*prece_cena/100*60
        elif vai_ir_karte == 'n':
            cena = cik_prece*prece_cena
        else:
            print('ievadi pareizus datus!')
            
    elif Kura_veikala == 'Top':
        prece = input('kādu preci jūs pirksiet? ') 
        cik_prece = int(input('Cik šo preci jūs pirksiet?(paciņu skaits)')) 
        prece_cena = float(input('kāda cena ir precei? (eiro) '))
        viss_nopirkts = input('Vai nopirkts viss kas sarakstā  (j/n)? ') 
        cena = cik_prece*prece_cena
    elif Kura_veikala == 'Lats':
        prece = input('kādu preci jūs pirksiet? ') 
        cik_prece = int(input('Cik šo preci jūs pirksiet?(paciņu skaits)')) 
        prece_cena = float(input('kāda cena ir precei? (eiro) '))
        viss_nopirkts = input('Vai nopirkts viss kas sarakstā  (j/n)? ') 
        cena = cik_prece*prece_cena
    elif Kura_veikala == 'Elvi':
        prece = input('kādu preci jūs pirksiet? ') 
        cik_prece = int(input('Cik šo preci jūs pirksiet?(paciņu skaits)')) 
        prece_cena = float(input('kāda cena ir precei? (eiro) '))
        viss_nopirkts = input('Vai nopirkts viss kas sarakstā  (j/n)? ') 
        cena = cik_prece*prece_cena

    else:
        print('Ievadi pareizus datus!')















        


        print('Formatēts x: ' "%.2f"%cena)
        print('Prieks sadarboties!')


