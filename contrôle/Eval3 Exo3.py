import random

repeat = True

while True:
    nombre_1 = random.randint(1, 10)
    nombre_2 = random.randint(1, 10)

    print('La somme entre', nombre_1, 'x', nombre_2, '?')
    
    reponse_enfant = int(input('Ecrire la réponse : '))
    
    if(nombre_1 * nombre_2 == reponse_enfant):
        print('Vous êtes correcte !!')
        print('Vous voulez continuez ?')
        verif=input('[y] or [n] : ')
        if(verif=='y'):
            print('OK !')
        elif(verif=='n'):
            print('à la prochaine :)')
            break
    else:
        print('C est faux, mais vous pouvez ressayez')
        verif=input('[y] or [n] : ')
        if(verif=='y'):
            print('Bonne chance! ^^')
        elif(verif=='n'):
            print('Au revoir. :( ')
            break