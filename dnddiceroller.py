import random
y = input("what no. dice?")
x = y.split("d")
j = int(x[1])
f = int(x[0])
total = 0
while f > 0:
    result = random.randint(1,j)
    print(result)
    total = total + result
    f=f-1
print("total = ", total)
