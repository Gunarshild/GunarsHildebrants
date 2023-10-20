
cukurs = 1.3, ('eiro/1kg')
udens = 0.0, ('eiro/ml')
citrons = 0.86, ('eiro/kg')                   #cik kas maksā
mandeļa_ekstrakts = 9.67, ('eiro/118ml')
kanelis = 0.63, ('eiro/25g')


recepte_aboli = float(input('cik kg ābolu vajag receptei? (kg) '))
recepte_cukurs = float(input('cik kg cukura vajag receptei? (kg) '))
recepte_udens = float(input('cik ml ūdens vajag receptei? (ml) '))
recepte_citrons = float(input('cik citronus vajag receptei? (gab) '))
recepte_mandelu_ekstrakts = float(input('cik ml mandeļu ekstraktu vajag receptei? (ml) '))          #cik ko vajag receptei
recepte_kanelis = float(input('cik g kanēļa vajag receptei? (g) '))

cik_ir_aboli = float(input('cik kg ābolu jums ir? (kg) '))
cik_ir_cukurs = float(input('cik kg cukura jums ir? (kg) '))
cik_ir_udens = float(input('cik ml ūdens jums ir? (ml) '))
cik_ir_citrons = float(input('cik citronus jums ir? (gab) '))
cik_ir_mandelu_ekstrakts = float(input('cik ml mandeļu ekstraktu jums ir? (ml) '))          #cik sastāvdaļas ir
cik_ir_kanelis = float(input('cik g kanēļa jums ir? (g) '))


if recepte_aboli < 0 or recepte_cukurs < 0 or recepte_udens < 0 or recepte_citrons < 0 or recepte_mandelu_ekstrakts < 0 or recepte_kanelis < 0 or cik_ir_aboli < 0 or cik_ir_cukurs < 0 or cik_ir_udens < 0 or cik_ir_citrons < 0 or cik_ir_mandelu_ekstrakts < 0 or cik_ir_kanelis < 0:
    print('Ievadiet pareizus datus!')
else:
    recepsu_skaits = recepte_aboli / cik_ir_aboli
    cena1r = (recepte_cukurs-cik_ir_cukurs*cukurs)+(recepte_citrons-cik_ir_citrons*citrons)+(recepte_mandelu_ekstrakts-cik_ir_mandelu_ekstrakts*mandeļa_ekstrakts)+(recepte_kanelis-cik_ir_kanelis*kanelis)
    cena = recepsu_skaits*cena1r
    print(cena,'eiro')

