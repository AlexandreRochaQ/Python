
email = ""
bool = False

while bool == False:
    email = input("Donner un email : ")
    for i in email:
        if(i == '@'):
            bool = True
    
print('Votre adresse est', email, 'merci.')

#======================
email=''

while not '@' in email:
    email = input('Donnez une adresse mail : ')
    
print('votre email est : ', email)