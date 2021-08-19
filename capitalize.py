s = "vikas    bha"
a = s.split(' ')
print(a)
for i in range(len(a)):
    a[i]= a[i].capitalize()
    b = ' '.join(a)
print(b)
