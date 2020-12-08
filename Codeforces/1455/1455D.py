t = int(input())
while t > 0:
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(1, len(a)):
        if a[i] < a[i - 1]:
            left = -1
            for j in range(i):
                if a[j] > x:
                    left = j
                    break
            if left == -1:
                print(-1)
                break
            for j in range(left, i + 1):
                if x == a[j]:
                    continue
                if x < a[j]:
                    #@#
                    left = i + 2
                    break
                a[j], x = x, a[j]
                ans += 1
    for i in range(1, len(a)):
        if a[i] < a[i - 1]:
            print(-1)
            break
    print(a)
    print(ans)
