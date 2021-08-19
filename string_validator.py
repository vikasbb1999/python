if __name__ == '__main__':
    s = input()
    t1, t2, t3, t4, t5 = False, False, False, False, False
    for i in s:
        print(i)
        if i.isalnum():
            t1 = True
        if i.isalpha():
            t2 = True
        if i.isdigit():
            t3 = True
        if i.islower():
            t4 = True
        if i.isupper():
            t5 = True
    print(f"{t1}\n{t2}\n{t3}\n{t4}\n{t5}")