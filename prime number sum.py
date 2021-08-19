take =  int(input())
take2 = []
val = 0
count = 0
for i in range(1,take+1):
    for j in range(2,i):
        if (i%j) == 0:
            break
    else:
        take2.append(i)

print(take2)
for i in take2:
    val += i
    for b in range(2,val):
        if (val%b) == 0:
            break
    else:
        if val < take:
            count += 1


print(count)