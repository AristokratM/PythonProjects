t = int(input())

while t:
    t -= 1
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a = sorted(a, reverse=True)
    ans = 0
    if k == 0:
        print(a[0] - a[-1])
    else:
        for i in range(k+1):
            ans += a[i]
        print(ans)