x = int(input())
y = int(input())
z = int(input())
n = int(input())
lst = []
for i in range(x+1):
    for j in range(y+1):
        for k in range(z+1):
            if i+j+k != 2:
                lst.append([i,j,k])

print(lst)