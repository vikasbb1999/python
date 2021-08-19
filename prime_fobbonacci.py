n1 = 30
n2 = 70
lst1 = []
lst2 = []
lst3 = []
lst4 = []
for i in range(n1,n2+1):
    if i >1:

        for a in range(2,i):
            if (i%a) == 0:
                break
        else:
            lst1.append(i)
print(lst1)



for a in lst1:
    for b in lst1:
        if a != b:
            c = str(b)
            d = str(a)
            e = d + c
            lst2.append(e)


print(lst2)

for i in lst2:
    i = int(i)
    for ii in range(2,i):
        if (i%ii) == 0:
            break
    else:
        lst3.append(i)

for v in lst3:
    if v not in lst4:
        lst4.append(v)
print(lst4)
maax = max(lst4)
miin = min(lst4)

print(miin)
print(maax)
print(len(lst4))

for i in range(len(lst4)-2):
    sum1 = miin + maax
    miin = maax
    maax = sum1

print(sum1, end="")
print()
print(len(lst4))
print(len(lst2))
