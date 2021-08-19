test_case = int(input())
while test_case >=1:
    count = 0
    n = int(input())
    if 0 < n <= 5000:
        while n > 0:
            n = n//2
            count +=1
    test_case -=1
    print(count)