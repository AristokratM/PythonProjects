n = int(input())
while n > 0:
    x = int(input())
    k = 0
    while 10 ** k <= x:
        k += 1
    print(k)
    n -= 1
