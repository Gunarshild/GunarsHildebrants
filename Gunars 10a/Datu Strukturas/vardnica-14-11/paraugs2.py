valstis = {
    'Somija':['Helsinki','Tampere','Rovaniemi','Kemijarvi','Jyvaskyle'],
    'Norvēģija':['Oslo','Bargana','Trumse','Arendāle','Molde'],
    'Dānija':['Kopenhāgena','Ronne','Odense','Pilsēta','Valsts'],
}



#izdrukāt vārdnīcas elementus, piekļūstot vārdnīcā konkarētai atslēgai
for i in valstis['Somija']:
    print(i)

for i in valstis['Norvēģija']:
    print(i)

for i in valstis['Dānija']:
    print(i)

#Izdrukāt pirmās 3 pilsētas Somijas
print(valstis['Somija'][:3])

#iegūt pēdējās 2 pilsētas Norvēģija
print(valstis['Norvēģija'][-2:])

#visas pilsētas no somijas, izņemot 3 pēdējās
print(valstis['Somija'][:3])

#iegūt no 2.-5.pilsētai no Dānijas
print(valstis['Dānija'][1:5])
