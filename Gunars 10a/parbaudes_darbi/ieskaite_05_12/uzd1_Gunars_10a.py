from decimal import * 

gads = int(input('Ievadi gadu: '))
vai_simtgade = gads/100
ja_simtgade = gads/400
ja_nav_simtgade = gads/4
if isinstance(print(Decimal(vai_simtgade)), int): # jo ja ir simtgade tad jādalās ar 400
    if isinstance(print(Decimal(ja_simtgade)), int):
        print(gads,'ir garais gads.')
    elif isinstance(print(Decimal(ja_simtgade)), float):
        print(gads,'ir īsais gads.')
elif isinstance(print(Decimal(vai_simtgade)), float):
    if isinstance(print(Decimal(ja_nav_simtgade)), int):
        print(gads,'ir garais gads.')
    elif isinstance(print(Decimal(ja_nav_simtgade)), float):
        print(gads,'ir īsais gads.')