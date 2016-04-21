elements = []
elements.append([])
elements.append([])
elements[0].append("jeff")
elements[0].append(16)
elements[0].append(14)
print(elements[0][0])
print(elements[0][2])
elements[0][2] = 12
print(elements[0][2])

a = {}
k = 0
while k < 10:

    key = k

    value = k+1
    a[key] = value
    k += 1
print(a)
