import random

print("EXERCICE 1! \n")

print("saisir 3 nombre réels ")

nombre_1 = float(input())
nombre_2 = float(input())
nombre_3 = float(input())

if nombre_1 == 0:
    print("Nombre 1 est nul")
if nombre_2 == 0:
    print("Nombre 2 est nul")
if nombre_3 == 0:
    print("Nombre 3 est nul")
    

print("La somme :", nombre_1+nombre_2+nombre_3)

print("Leur produit ", nombre_1*nombre_2*nombre_3)

print("Leur moyenne ", (nombre_1+nombre_2+nombre_3)/3)

print("Le quotient ", (nombre_1+nombre_2)/nombre_3)

print("EXERCICE 2! \n")

prixProduit = input("Le prix d'un produit ? saisir: ")
RedOuAug = input("Il s'agit d'une réduction ou augmentation? saisir: ")
taux = input("Le taux ? saisir: ")

if(RedOuAug == "réduction"):
    print("prix initial", prixProduit)
    print("Réduction de ", taux)
    taux = taux/100
    prixProduit = prixProduit-(taux*prixProduit)
    print("Prix final ", prixProduit)
else:
    if RedOuAug == "augmentation":
        print("prix initial", prixProduit)
        print("Augmentation de ", taux)
        taux = taux/100
        prixProduit = prixProduit+(taux*prixProduit)
        print("Prix final ", prixProduit)
    
print("EXERCICE 3! \n")

des_1 = random.randint(1,6)
des_2 = random.randint(1,6)

print("Vos dés sont", des_1, des_2)

if des_1 == des_2:
    points = (des_1 + des_2) * 2
    
else:
    if (des_1 == 1 and des_2 != 1) or (des_1 != 1 and des_2 == 1):
        points = 0
        
print("vos points : ", points)
