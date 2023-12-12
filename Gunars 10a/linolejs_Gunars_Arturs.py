import math
vai_vel_pasutijumus = 'j'
while vai_vel_pasutijumus == 'j': #Lai var vairāksas reizes pasūtīt
    veikals = input('Kādā veikalā jūs vēlaties pirkt?: ')
    linoleja_maksa = float(input('Cik maksās 1m^2 linolejs? (eiro): '))
    rula_platums = float(input('Cik plats ir viens rulis? (m): '))
    telpas_platiba = float(input('Cik plata ir grīda? (m): '))
    telpas_gara = float(input('Cik gara ir grīda? (m): '))
    vai_apaksklajs = input('Vai jūs liksiet apkakšklāju (j/n): ')
    telpas_laukums = math.ceil(telpas_platiba)*math.ceil(telpas_gara)
    izmaksas = telpas_laukums*linoleja_maksa                               #aprēķini
    pari_paliek = telpas_laukums-(telpas_gara*telpas_platiba)
    if vai_apaksklajs == 'n':#ja nebūs apakšleja
        print('-----------------------------------------')
        print(f'Linoleja cena(m^2):  {linoleja_maksa} eiro\nKopēja izmaksa: {izmaksas} eiro\nAtlikums linoleja: {round(pari_paliek,2)} m^2\nPirkts: {veikals} ') #čeks
        print('-----------------------------------------')
        vai_vel_pasutijumus = input('Vai jūs vēl vēlaties pasūtīt citus linoleja komplektus? (j/n): ')
    elif vai_apaksklajs == 'j':#ja būs apakšleja
        apaksklaja_maksa = float(input('Cik maksā 1m^2 apakšklājs? (eiro): '))
        izmaksas += telpas_laukums*apaksklaja_maksa
        print('-----------------------------------------')
        print(f'Linoleja cena(m^2):  {linoleja_maksa} eiro\nApakšlejas cena(m^2): {apaksklaja_maksa} eiro\nKopēja izmaksa: {izmaksas} eiro\nAtlikums linoleja: {round(pari_paliek,2)} m^2\nPirkts: {veikals}') #čeks
        print('-----------------------------------------')
        vai_vel_pasutijumus = input('Vai jūs vēl vēlaties pasūtīt citus linoleja komplektus? (j/n): ')