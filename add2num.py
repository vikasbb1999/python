l1 = input()
l2 = input()
l1 = l1[1:-1].split(",")
l2 = l2[1:-1].split(",")
k = ""
m = ""
aa = ""
lst = []
for i in l1:
    k += str(i)
for j in l2:
    m += str(j)
n = int(k) + int(m)
work = 1
n = str(n)[::-1]
for i in n:
    lst.append(i)
print(lst)
