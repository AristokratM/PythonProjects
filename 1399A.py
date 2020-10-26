t = int(input())
while t:
    t -= 1
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    i = 0
    j = len(a) - 1
    b = True
    while i < j:
        if a[i] + 1 < a[i+1]:
            b = False
            break
        if a[j] - 1 > a[j-1]:
            b = False
            break
        i += 1
        j -= 1
    #    print(i, j)
    if b:
        print("YES")
    else:
        print("NO")
