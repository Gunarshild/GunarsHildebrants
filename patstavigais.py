'''Izveidot 3 sarakstus: lietotajs pats norādīs,
cik elementus likt sarakstā.
>Pirmā un otrā saraksta vertības ievada lietotājs.
>Trešā saraksta vērtības iegūst apvienojot pirmos 2 sarakstus
>Katra saraksta saturu glīti parādīt uz ekrāna.'''

Pirmais_Saraksts = []
Otarais_saraksrts = []
Tresais_saraksts = []

Cik_gars1 = int(input('Cik elementi ir 1. sarakstā: '))
for a in range(1,Cik_gars1+1):
    kurs_elements = 'ievadiet ',a,' Elementu: '
    Elements = input(kurs_elements)
    Pirmais_Saraksts.append(Elements)

print('-------------------------------------------------------------')

Cik_gars2 = int(input('Cik elementi ir 2. sarakstā: '))
for b in range(1,Cik_gars2+1):
    kurs_elements = 'ievadiet ',b,' Elementu: '
    Elements = input(kurs_elements)
    Otarais_saraksrts.append(Elements)

print('-------------------------------------------------------------')

Tresais_saraksts = Pirmais_Saraksts + Otarais_saraksrts

print(Pirmais_Saraksts)
print(Otarais_saraksrts)
print(Tresais_saraksts)
