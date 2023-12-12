#izveidot vārdnīcu ar datiem par automašīnu(4)
auto = {
    'Zīmols': 'Volvo',
    'krasa': 'Balts',
    'Gads': 2021,
    'Modelis':'xc90'
}
dati = input('Ievadiet zīmolo, lai pārbaudītu: ')
if dati == auto['Zīmols']:
    print('Auto ir vārdnīcā! ')
elif dati == auto.values():
    print('Auto ir kā vērtība')
else:
    print('Auto nav')