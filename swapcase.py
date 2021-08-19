get = list(input().lower())
s = ""
start1 = 1
start0 = 0
if len(get)%2 == 0:
    for i in range(len(get)//2):
        x, y = get[start0], get[start1]
        s = str(s) +str(y) + str(x)
        start0+=2
        start1+=2
else:
    for i in range(len(get)//2):
        x, y = get[start0], get[start1]
        s = str(s) +str(y) + str(x)
        start0+=2
        start1+=2
    s += get[-1]


print(s)