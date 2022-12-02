stock = 1000 
production = 1000
liste_production = []
liste_stock = []

liste_stock.append(stock)
liste_production.append(production)

#================================ Question 1 et 2
for i in range(1, 10):
    production = production - (production*0.02)
    stock += production
    
    liste_stock.append(stock)
    liste_production.append(production)


print('Liste de production : ')

for i in range(10):
    print('Jour',i+1, ':', liste_production[i])
    
print('Liste de Stock')

for i in range(10):
    print('Jour', i+1, ':', liste_stock[i])
    
#================================ Question 3
production = 1000
jour = 0
while stock < 15000:
    production = production - (production*0.02)
    stock += production
    jour += 1

print(jour, 'jours sont necessaires pour avoir 15000L')
    
