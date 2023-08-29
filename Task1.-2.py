import itertools

list = ['0001','0011','0101','1011','1101','0111']

new_list = [int(binary , 2) for binary in list]

new_list.sort()

print(new_list)

sum= sum(new_list)

print(sum)

combination = itertools.combinations(new_list,2)

last = None

for combo in combination:
    last = combo
    print(combo)
    
if last != None:
    print(last[0])
    print(last[1])

# jo minus krane wala concpt hai vo karna hai like 2 array lekar ek mai sab add karke ek ek elemnt se subtract karna hai and phir itertools lagana hai

