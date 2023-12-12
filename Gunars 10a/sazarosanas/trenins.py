nenodots = input('vai jums ir kāds nenodots izdevums? (j/n)')
if nenodots == 'j':
    print('jūs nedrīkstat neko izņemt.')
elif nenodots == 'n':
    pieprasīts = input('Vai šī publikācija ir pieprasīta? (j/n)')
    if pieprasīts == 'j':
        print('izsniedz uz divām dienām')
    elif pieprasīts == 'n':
        zurnals = input('Vai publikācija ir žurnāls?')
        if zurnals == 'j':
            print('izsniedz uz 7 dienām')
        elif zurnals == 'n':
            students = input('vai jūs esat students? (j/n)')
            if students == 'j':
                print('izsniedz uz 14 dienām')
            elif students == 'n':
                print('izsniedz uz 28 dienām')