#mērķis ir uztaisīt programmu, kurā zemūdene spridzina burbuļus
#tiek skaitīti punkti
from tkinter import *
from random import *
from math import *
logs = Tk()
garums = 900
platums = 900
logs.title('Burbuļu spidzinātājs')
a = Canvas(logs, width=platums, height=garums, bg='lightblue')
a.pack()
kuga_id = a.create_oval(5,5,100,100,outline='darkblue',width=10)





mainloop()

