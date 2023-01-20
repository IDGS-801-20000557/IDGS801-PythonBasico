
nombres=["Juan","Mario","Laura"]
numeros=[1,2,3,4,5]

datos=[1,2.5,"Mario",True]

nombres[0]="Roberto"

print(nombres)
print(nombres[:])
print(nombres[2])
print(nombres[:3])
print(nombres[1:])

nombres.append("Dario")
print(nombres)
nombres.insert(2,"Maria")
print(nombres)

nombres.extend(["chencha",2,23,5])
print(nombres)
nombres.remove("chencha")
print(nombres)
nombres.pop()
print(nombres)

n=["juan"]
n2=n*5
print(n2)
print(nombres)

del nombres[2]
print(nombres)