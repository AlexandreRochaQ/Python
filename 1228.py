while True:
   try: 
        n = int(input())
   except EOFError: 
        break
   saida = [int(x) for x in input().split()]
   chegada = [int(x) for x in input().split()]
   ans = 0
   while saida != chegada:
        for i in range(n):
            if saida[i] != chegada[i]:
                pos = chegada.index(saida[i])
                element = chegada[pos]
                chegada.remove(chegada[pos])
                chegada.insert(i, element)
                ans += pos-i
   print(ans)