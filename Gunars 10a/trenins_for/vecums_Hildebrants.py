SV = int(input('ievadiet sava suņa vecumu'))
if SV<=2 and SV>0:
    print('Šuņa vecums ir ',SV*10.5,'gadi.')
elif SV>2:
    print('Šuņa vecums ir ',(SV-2)*4+21,'gadi.')
else:
    print ('ievadi citus datus')