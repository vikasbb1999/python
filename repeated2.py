take = list(map(str, input()))
output = []
count = 0
if len(take) > 1:
    for h in range(len(take)//2):
        e0 = 1 + int(h)
        s0 = 0
        s1 = 1 + int(h)
        e1 = e0 + s1
        count = 0
        for i in range(len(take)//(1+int(h))):
            if take[s0:e0] == take[s1:e1]:
                count+=1
                if count == ((len(take)-1)//(1+int(h))):
                    output.append("True")
            elif s1 == (len(take)//2):
                output.append("False")

            s0 += 1
            e0 += 1
            s1 += 1
            e1 += 1
else:
    output.append("False")
print(output[-1])
