import random

coups = 0
score = 0
count = 0
num_hasard = random.randint(0, 100)

while coups != num_hasard:
    count +=1
    coups = int(input('Essayez un numero : '))
    
    if(coups < num_hasard):
        print('votre numero est plus petit')
    elif(coups > num_hasard):
        print('votre numero est plus grand')
    elif(coups == num_hasard):
        print('Vous avez trouvez le numero', num_hasard, '!!!!')
        score = count
        print('votre score est', score)
        
#=================================================

replay = input('Voulez-vous rejouer ?[y] ou [n] ')

if(replay == 'y'):
    num_hasard = random.randint(0, 100)
    count = 0
    
    while count < score:
        
        coups = int(input('Essayez un numero : '))
        count+=1
        
        if(coups < num_hasard):
            print('votre numero est plus petit que X')
        elif(coups > num_hasard):
            print('votre numero est plus grand que X')
        elif(coups == num_hasard):
            print('Vous avez trouvez le numero', num_hasard, '!!!!')
            score = count
            print('Votre score est', score)
            #================================================
            replay = input('Voulez-vous rejouer ?[y] ou [n] ')
            if(replay == 'y'):
                count = 0
            else:
                print('Merci, bonne journée')
                break
else:
    print('Merci, bonne journée')
        
    
    
