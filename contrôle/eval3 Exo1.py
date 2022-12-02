verif1 = False
verif2 = False

numero_debut = -1
numero_fin = -1

while (verif1 == False) and (verif2 == False):
    
    if(verif1 == False):
        while numero_debut <= 0:
            numero_debut = int(input('Ecrire un numero pour le debut : '))
            if(numero_debut < 0):
                print('Votre numéro est negatif')
            verif1 = True
            
    if(verif2 == False):
        while numero_fin <= 0:
            numero_fin = int(input('Ecrire un numero pour la fin : '))
            if(numero_fin < 0):
                print('Votre numéro est negatif')
            verif2 = True
            
    if(numero_debut > numero_fin):
        verif1 = False
        verif2 = False
        print('Votre fin est plus petit que le début, vous devez recommencer.')
        
calcule = 0

for x in range(numero_debut, numero_fin+1, +1):
    if(x%5==0):
        calcule = calcule + x
        
print('La somme totale est', calcule)