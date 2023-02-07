lista=[-4,3,-9,0,4,1]

positivo=0
negativo=0
nulo=0

for i in lista:
    if i == 0:
        nulo+=1
    else if i > 0:
        positivo+=1
    else:
        negativo+=1

positivo = positivo/len(lista)
negativo = negativo/len(lista)
nulo = nulo/len(lista)

print("Positivos: "+positivo+"/n"+
        "Negativo: "+negativo+"/n"+
        "Nulo: ",nulo)
