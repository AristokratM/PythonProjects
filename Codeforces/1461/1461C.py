t = int(input())
while t > 0:
    t -= 1
    n, m = map(int, input().split())
    lst = list(map(int, input().split()))
    lst.reverse()
    k = n
    for i in lst:
        if i == k:
            k -= 1
        else:
            break
    ans = 1.0
    for i in range(m):
        r, p = map(float, input().split())
        if r >= k:
            ans *= (1.0 - p)
    if k == 0:
        print(1)
    else:
        print("{:.6f}".format(1.0 - ans))
