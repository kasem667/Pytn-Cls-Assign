matrix = []
for row in range(5):
    Collumn = []
    for coll in range(5):
        num = int(input())
        Collumn.append(num)
    matrix.append(Collumn)

for x in range(3):
    line = matrix[x][:-x - 1]
    print(line)


'''



1	2	3	4	5
6	7	8	9	10
11	12	13	14	15
16	17	18	19	20
21	22	23	24	25

name = "kasem"
print(f"-{name}-")
print(name.lower())
print(name.upper())
print(f".{name}.")
lista = ""
for i in name:
    if name.index(i) == 0 or name.index(i) == (len(name)-1):
        lista += i.upper()
    else:
        lista += i
print(lista)



color("green")
begin_fill()
left(30)
forward(100)
circle(40, 180)
left(260)
circle(40, 180)
forward(100)
end_fill()
done()
'''