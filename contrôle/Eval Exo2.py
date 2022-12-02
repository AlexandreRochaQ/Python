compte_epargne = 50
taux = 0.25

for i in range(1, 18):
    compte_epargne = compte_epargne + (50 + (compte_epargne * taux))

if(compte_epargne < 699.99):
    print('L argent n est pas suffisante')
elif(compte_epargne < 999,99):
    print('Il peut acheter la Nakamura E-Cliff LTD')
elif(compte_epargne < 1499.99):
    print('Il peut acheter la Nakamura E-Crossover S')
elif(compte_epargne >=1499.99):
    print('Il peut acheter la Nakamura E-Fit 150')
    
# juste pour savoir son compte bancaire.
compte_epargne = (round(compte_epargne, 2))
print('Son compte bancaire actuelle est : ', compte_epargne)