test = int(input())
o = []
if 1 <= test <= 10:
    b = []
    c = []
    for i in range(test):
        player = int(input())
        if 1 <= player <= 1000:
            b = list(map(int,input().split()))[:player]
            c = list(map(int,input().split()))[:player]

        start = 0
        end = 1
        win = []
        lose = []
        for i in b[start:end]:
            for j in c[start:end]:
                if int(i) < int(j):
                    win.append(1)
                elif int(i) > int(j):
                    lose.append(1)
                start += 1
                end += 1
        if len(win) > len(lose):
            o.append("WIN")
        else:
            o.append("LOSE")

for i in o:
    print(i)
"""1
6
112 243 512 343 90 478
500 798 234 400 452 150
"""