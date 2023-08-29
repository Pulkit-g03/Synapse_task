jumbled_superheros=['DocTor_sTRAngE','sPidERmaN','MoON_KnigHT','caPTAIN_aMERIca','hULK']
indices=[]
decoded_names=[]

for index, heros in enumerate(decoded_names):
    indices.append(index)
    print(indices,heros)

decoded_names=[heros.replace("_"," ") for heros in jumbled_superheros]
decoded_names=[heros.lower() for heros in decoded_names]

Len_lambda = lambda hero:len(hero)

name_length = list(map(Len_lambda, decoded_names))

indices=list(range(len(decoded_names)))
indices.sort(key=lambda index:name_length[index])


for index in indices:
    print(decoded_names[index].title())
