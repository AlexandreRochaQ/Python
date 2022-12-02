def livretA(montant, taux, duree):
    for i in range (duree):
        total = montant * (1+taux/100)
        
    return (total)
    

montantInitial = (int(input()))
tauxA = (int(input()))
annes = (int(input()))

total = livretA(montantInitial, tauxA, annes)

print("montant à déposer :", montantInitial)
print("Taux du livret A:", tauxA)
print("La durée :", annes)

for i in range(annes):
    print('Solde du livret,' i, "annés(s):', total)

