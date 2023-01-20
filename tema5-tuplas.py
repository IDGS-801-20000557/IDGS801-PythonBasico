

tupla=(1,2,3)
print(tupla)
print(type(tupla))
tupla2=(7,"Roberto",True,23.8,16+7j)

print(tupla2)

print(tupla2[1])

print(tupla2[4])
print(tupla2[-1])
print(tupla2[0:3])
print(tupla2[:3])
print(tupla2[3:])

a,b,c=tupla

d=tupla[1]
print(a)
print(c)
print(d)
tuplaN=tupla+tupla2
print(tuplaN)
print(tupla.count(2))

tupla[2]=23