def premier_groupe(verbe):  
    if verbe[-2] == 'e' and verbe[-1] == 'r':                                                 
        return True
    else:
        return False
#=================

def voyelles(verbe):
    com = 0
    
    for x in verbe:
        if x == 'a' or x == 'e' or x == 'i' or x == 'o' or x == 'u' or x == 'y':
            com+=1;
        
    return com

#===================

def maj(verbe):
    for i in verbe:
        phrase+=ord[i+32]
        
    return phrase
        

#===================

v = input('Donner un verbe : ')
verif = premier_groupe(v)

if verif == True:
    print(v, 'est un verbe du premier groupe')
else:
    print(v, 'n est pas un verbe du premier groupe')
    
#====================

v2 = input('Donner une voyelle : ')

voy = voyelles(v2)   

print('Le nombre des voyelles est :', voy)

#===================

v3 = input('Donner une phrase minuscule : ')

phraseMaj = maj(v3)

print('Votre phrase en Majuscule : ', phraseMaj)
