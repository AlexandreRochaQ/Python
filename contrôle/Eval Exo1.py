age_Lise = int(input('Ecrire l âge de Lise : '))

compte_bancaire = 100

for i in range(2, age_Lise+1):
    compte_bancaire += 100 + (2*i)
    
print('Elle aura :', compte_bancaire)