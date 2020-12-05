import math
t = int(input())



while t:
    t -= 1
    n = int(input())
    a = list(i for i in range(1, n+1))
    print(2)
    while len(a) > 1:
        k1 = a.pop()
        k2 = a.pop()
        print(k1, k2)
        a.append(int(math.ceil((k1+k2)/2.0)))




