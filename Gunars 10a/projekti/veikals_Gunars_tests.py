stop = '0'
ceks = 'Iepirkšanas čeks: '  #izveidots lai katrreiz nav jāatkārto teksts
summa_bez_atlaides = 0.0
kopsumma = 0.0 #galējā summa

while stop == '0':
    ceks = '\n\n'

    precu_skaits = int(input('Ievadiet preču skaitu: '))
    if precu_skaits < 0:
        exit()
    produkts = input('Ievadiet preces nosaukumu:  ')
    produkta_cena = round(float(input('Ievadiet cenu 1 gab cenu: ')),2) # lai būtu divi skaitļi aiz komata

#atlaides var izvēlēties, ierakstot skaitli no 1-5
    print('\n1-Maxima: 30% atlaide\n2-Elvi: 40%, ja ir klienta karte\n3-Rimi: 20%, bet 50%, ja ir klienta karte\n4-Mego: 30%, ja pērk 3 un vairāk preces\n5-Aibe:katra katra 2.prece par brīvu')
    atlaides_veids = input('Izvēlieties kurā veikalā iepirkieties (Rakstiet ciparu no 1 - 5)')

    cena_bez_atlaides = produkta_cena*precu_skaits #iegūst cenu bez atlaidēm
    pirkuma_cena = cena_bez_atlaides #no pirkuma cenas rēķinās atlaides
#sākās atlaižu aprēķināšana
    if atlaides_veids == '1':#atlaide Maximā
        #pirkuma_cena = pirkuma_cena*0.7
        pirkuma_cena*=0.7 # izmantosalikto operātoru
    elif atlaides_veids == '2':#atlaide elvi
        klienta_karte = input('Ievadiet 1, ja ir klienta karte, 0 ja nav: ')
        if klienta_karte == '1':
            pirkuma_cena*=0.6#atlaide 40%
    elif atlaides_veids == '3':#atlaide Rimi
        klienta_karte = input('Ievadiet 1, ja ir klienta karte, 0 ja nav: ')
        if klienta_karte == '1':
            pirkuma_cena*=0.5#atlaide 50%
        else:
            pirkuma_cena*=0.8
    elif atlaides_veids == '4':
        if precu_skaits >=3:
            pirkuma_cena*=0.7
    elif atlaides_veids == '5':
        if precu_skaits%2==0:
            pirkuma_cena/2
        else:
            #ATŅEM 1 GABALA CENU NO KOPĒĀS CENAS
            pirkuma_cena -= produkta_cena
            pirkuma_cena/=2
            #ja ir nepāra skaitlis gabalu 
            #pēc tam atņem atņem katru otro produktu
    cena_bez_atlaides = round(cena_bez_atlaides,2)
    pirkuma_cena = round(pirkuma_cena,2) #noapaļo ar 2 cipariem aiz komata

    summa_bez_atlaides+=cena_bez_atlaides #iegūst summu
    kopsumma+=pirkuma_cena

    ceks+=produkts+'\n'+str(produkta_cena)+' X '+str(precu_skaits)+'\t\t\t\t'+str(cena_bez_atlaides)+'\nAr atlaidi\t\t\t'+str(pirkuma_cena)
    stop = input('Viss nopirkts? Jā - 1 Ne - 0 ')
ceks+='\n\n--------------------------------\n\n'
ceks+=f'Kopā bez atlaides(EUR:)\t{summa_bez_atlaides}\nKopā ar atlaidēm(EUR:)\t\t{kopsumma}\n\n'
ceks += f'Kopā apmaksai (EUR):\t\t{kopsumma}'
print(ceks)