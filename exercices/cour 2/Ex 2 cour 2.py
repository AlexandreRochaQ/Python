def culture(bacteries, N):
    for t in range(1,N+1):
        bacteries = 2*bacteries-t
    return bacteries

nb_bacteries = int(input('donner le nombre de bactéries initial :'))

N = int(input('Dans combien de secondes: '))

for i in range(1, N+1):
    bact = culture(nb_bacteries, i)
    print('à l instant t=', i, 's:', bact)


while nb_bacteries<20000:
    t=t+1
    nb_bacteries=2*nb_bacteries-t
    
print(t)
print(nb_bacteries)