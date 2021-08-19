lit = [-10,-1,-2,3,4,5,-63,21,3]
lit.sort()
print(lit)
a = lit[0]
n = 0
for i in lit:
    if a < i:
        a = i
        print(a)
        break
