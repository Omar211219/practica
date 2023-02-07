lista=[1,3,1]
var=0

for i in lista:
    if lista.count(i) == 3:
        print(i*lista.count(i))
        var=1
        break
    else if lista.count(i) == 2:
        print(i*lista.count(i))
        var=1
        break

if var==0:
    print(max(lista))
