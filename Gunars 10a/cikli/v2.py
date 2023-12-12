'''atbilde = 'j'
while atbilde == 'j':
    print('nekustties')
    atbilde = input('Vai briesmonis ir draudzīks?(j/n)')
print('Bēdz prom!')'''

#pārbaudiet vai lietotājs prot reizināt ar 7
#progrmma atkārton darbību līdz brīdim, kad uzdoti visi 12 jautājumi
#jal litotājs uzraksta stop progrmma beidzas
#ja ir nepareizi tad atgriežas pie jautājuma
#reizinātāju ievada lietotājs

reiz = int(input())
for i in range(1,13):
    print('Cik ir',i,'x',reiz,'?')
    minejums = input()
    if minejums == 'stop':
        break
    if minejums == 'izlaist':
        continue
    atb = i * reiz
    if int(minejums) == atb:
        print ('pareiza atbilde!')
    else:
        print ('Nē, tas ir',atb)