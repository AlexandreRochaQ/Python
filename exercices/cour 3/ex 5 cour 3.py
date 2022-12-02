billes = 1000 
etage = 0

while billes > 0:
    etage = etage+1
    billes = billes-etage**2
    
print('il faut', etage, 'etages')

