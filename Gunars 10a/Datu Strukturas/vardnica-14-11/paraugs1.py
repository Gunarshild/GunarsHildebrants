telefons = {
    'Jānis':26738193,
    'Rita':29372934,
    'Anna':28352781
    }
#Jānim ir divi telefona nummuri
telefons.update({'Jānis':22222222})
print('Šis ir Ritas nummurs',telefons['Rita'])
print('Šis ir Jāņa nummurs',telefons['Jānis'])
print('Šis ir Annas nummurs',telefons['Anna'])


#Izveidot vārdnīcu ar atslēgu virkni un fromkeys() metodi
#Vārrdnīcu nenorādot ierakstu vētības
kk = ('viens','divi','trīs')
dd = dict.fromkeys(kk)
print(dd)
val = 0 #šī vērtība būs visai vārdnīcai
dd = dict.fromkeys(kk,val)
print(dd)

print('---------------------------------------------------------------------------')

#izveidot cvārdnīcu, kas satur sarakstu
valstis = {
    'Somija':['Helsinki','Tampere','Rovaniemi'],
    'Norvēģija':['Oslo','Bargana','Trumse'],
    'Dānija':['Kopenhāgena','Ronne','Odense'],
}

for atslega, vertiba in valstis.items():
    for i in vertiba:
        print("{}: {}".format(atslega,i))
    print('-------------------')