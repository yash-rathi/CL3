bits = 4
length = (2 * bits) + 1

def dec2Bin(num):
    a = [0 for i in range(4)]
    
    i = bits - 1
    while(i >= 0):
        a[i] = num % 2
        num = num / 2
        i -= 1
    return a

def add(a, b):
    c = 0
    s = [0 for i in range(length)]
    
    i = length - 1
    while(i >= 0):
        temp = a[i] + b[i] + c
        s[i] = temp % 2
        c = temp / 2
        i -= 1
    return s

def ars(num):
    i = length - 1
    while(i >= 1):
        num[i] = num[i - 1]
        i -= 1
    return num

def booths(num1, num2):
    a = dec2Bin(num1)
    b = dec2Bin(num2)
    x = dec2Bin(- num1)
    
    A = [0 for i in range(length)]
    S = [0 for i in range(length)]
    P = [0 for i in range(bits)]
    
    for i in range(bits):
        A[i] = a[i]
        S[i] = x[i]
        P.append(b[i])
    P.append(0)
    
    print "A = ", A
    print "S = ", S
    print "P = ", P
    
    for i in range(bits):
        print i, ")"
        if((P[-2] == 0 and P[-1] == 0) or (P[-2] == 1 and P[-1] == 1)):
            P = ars(P)
            print P
        elif(P[-2] == 0 and P[-1] == 1):
            P = add(P, A)
            print P
            P = ars(P)
            print P
        elif(P[-2] == 1 and P[-1] == 0):
            P = add(P, S)
            print P
            P = ars(P)
            print P
        print ""
    return P