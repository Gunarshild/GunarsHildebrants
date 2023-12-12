vai_grib_turpinat = 'j'
merijumi = {
    '1': 172,
    '2': 185,
    '3': 164,
    '4': 184,
    '5': 162,
    '6': 164,
    '7': 165,
    '8': 167,
    '9': 177,
    '10': 184,
    '11': 165,
    '12': 180
}

while vai_grib_turpinat == 'j':

    for kartas_skaitlis, merijums in merijumi.items():#Izprintē vārdnīcu stabiņā uz leju
        print(kartas_skaitlis, ":", merijums)
    vai_grib_redzet = input('Vai tu gribi redzēt vidējo augumu? (j/n)')
    if vai_grib_redzet == 'j':
        videjo = sum(merijumi.values())/len(merijumi)
        print(f'videjais ir {round(videjo,2)}')
    ko_grib_darit = input('Ja jūs gribat pievienot spieiet 1\nJa jūs gribat dzēst spieiet 2\nJa jūs gribat redzēt visus datus spieiet 3\n')
    print('----------------------------------------')
    if ko_grib_darit == '1':
        ievade_atsl = input('Ievadiet kārtas numuru: ')
        if ievade_atsl == 'stop':
            exit('Paldies ka jūs izmantojāt šo programmu!')
        ievade_vert = int(input('Ievadiet merijumu: '))
        if ievade_vert == 'stop':
            exit('Paldies ka jūs izmantojāt šo programmu!')
        merijumi[ievade_atsl] = ievade_vert #Ievieto atslēgu un vērtību vārdnīcā
        print(f'pievienoja {ievade_atsl}:{ievade_vert}') #Pārāda ko ievietoja
        for kartas_skaitlis, merijums in merijumi.items():#Izprintē vārdnīcu stabiņā uz leju izmainīto
            print(kartas_skaitlis, ":", merijums)
        print('----------------------------------------')
        vai_grib_turpinat = input('Vai jūs gribat turpināt? (j/n)')
    elif ko_grib_darit == '2':
        ko_iznemt = input('kuru pēc kārtas izņemt? ')
        if ko_iznemt == 'stop':
            exit('Paldies ka jūs izmantojāt šo programmu!')
        else:
            iznema = merijumi.pop(ko_iznemt)
            print('izdzesa',iznema,'\n','pēc kārtas',ko_iznemt,'.')#Pārāda ko izņēma
            for kartas_skaitlis, merijums in merijumi.items():#Izprintē vārdnīcu stabiņā uz leju izmainīto
                print(kartas_skaitlis, ":", merijums)
            print('----------------------------------------')
        vai_grib_turpinat = input('Vai jūs gribat turpināt? (j/n)')
    elif ko_grib_darit == 'stop':
        exit('Paldies ka jūs izmantojāt šo programmu!')