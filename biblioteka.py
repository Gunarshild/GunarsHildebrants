#bibliotēkas sistēma
PI = 2 #Pieprasīts Izdevums
NPIP = 28 #Nav Pieprasīts Izdevums Personāls
NPIS = 14 #Nav Pieprasīts Izdevums Students
ZNPI = 7 #Žurnāls Nav Pieprasīts Izdevums
#Ja personālam nav laikā nodots nedod neko



VIP = input('Vai jūs esat personāls? ') # vai ir personāls
if VIP == ('jā'):
    VING = input('Vai ir nodotas grāmatas? ') #vai ir nodotas grāmatas
    if VING == ('nē'):
        print('Nevar dabūt neko')
    elif VING == 'jā':
        ZVG = input('Grāmata vai žurnāls? ') #Grāmata vai žurnāls
        if ZVG == ('žurnāls') and VIP == ("jā"):
            print('Var ņemt uz 7 dinām')
        elif ZVG == ('grāmata'):
            GIP = input('Grāmata ir pirprasīta? ')
            if ZVG == ('grāmata') and VIP == ("jā") and GIP == ('jā'):
                print('Var ņemt uz 2 dinām')
            elif ZVG == ('grāmata') and VIP == ("jā") and GIP == ('nē'):
                print('Var ņemt uz 28 dinām')
elif VIP == 'nē':
    VING = input('Vai ir nodotas grāmatas? ') #vai ir nodotas grāmatas
    if VING == ('nē'):
        print('Nevar dabūt neko')
    elif VING == 'jā':
        ZVG = input('Grāmata vai žurnāls? ') #Grāmata vai žurnāls
        if ZVG == ('žurnāls') and VIP == ("nē"):
            print('Var ņemt uz 7 dinām')
        elif ZVG == ('grāmata'):
            GIP = input('Grāmata ir pirprasīta? ')
            if ZVG == ('grāmata') and VIP == ("nē") and GIP == ('jā'):
                print('Var ņemt uz 2 dinām')
            elif ZVG == ('grāmata') and VIP == ("nē") and GIP == ('nē'):
                print('Var ņemt uz 14 dinām')







