lista = []
turn = int(input())
for i in range(turn):
    num = int(input())
    lista.append(num)

for x in lista:
    if x>120:
        break
    else:
        if x%10==0:
            print(x)

