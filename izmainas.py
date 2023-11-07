Saraksts = [3,6,1,9,7,4,8]
Saraksts.append('Cepums')  #ar append pievieno beigās
print(Saraksts)

Saraksts.pop() #pop izmet no beigām
print(Saraksts)

Saraksts.insert(3, 'Hello!') #ievieto 3. no kreisās
print(Saraksts)

Saraksts.remove(4) #izdzēš norādīto elementu
print(Saraksts)

#izdzeš vienu elementu
tests = [1,2,3,4,5,6,7,8]
del tests[2]
print(tests)

del tests[3:6]
print(tests) #izdzēš intervālu

cipari = [1,2,3,4,5,6,7,8]
del cipari[2:7:2] #no 2-7 elementam dzēš ārā katru otro sākot ar 2
print(cipari) 