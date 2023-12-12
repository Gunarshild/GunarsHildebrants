import math 
import random
skaitlis = 43.7
print('Noapaļots uz leju:',math.floor(skaitlis))
print('Noapaļots uz augšu:',math.ceil(skaitlis))

print('Mainīgā pakāpe',math.pow(skaitlis,2))
print(math.pow(4,6)) #pirmais sk tas ko kāpina, otrais kurā pakāpē
pakape = 3
print(math.pow(skaitlis,pakape))
print('kvadrātsakne:',math.sqrt(skaitlis))

x = 256971/2541
print('x:',x)
print('Formatēts x: ' "%.3f"%x)
print('Formatēts x: ' "{:.2f}".format(x))

cipars = random.random()  #0.1 - 1.0
print(cipars)

cipars2 = random.randint(1,50)
print(cipars2)
