import random
#akmens šķēres papīrs\
gajieni = ['akmens','papīrs','šķēres'] #saraksts
while True:
    cilveka_gājiens = input('Ievadi savu gājienu:')
    datora_gajiens = random.choice(gajieni)
    print('Cilvēks:',cilveka_gājiens, 'vs dators:',datora_gajiens)
    if cilveka_gājiens == datora_gajiens:
        print('neizšķirts')
    elif cilveka_gājiens == 'akmens' and datora_gajiens == "šķēres":
        print('Ciklvēks uzvar!')
    elif cilveka_gājiens == 'šķēres' and datora_gajiens == "papīrs":
        print('Ciklvēks uzvar!')
    elif cilveka_gājiens == 'papīrs' and datora_gajiens == "akmens":
        print('Ciklvēks uzvar!')
    else: 
        print('Dators uzvar')
