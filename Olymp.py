def D():
    n = int(input())
    k = 10 ** n
    lb = 10 ** (n-1)
    ans = 0
    for i in range(int(k ** 0.5 ) + 1):
        if lb <= i * i < k:
            ans += 1
    print(ans)


def E():
    m = int(input())
    print(1 + m // 60 // 24, m // 60 % 24, m % 60)


def F():
    a, b = map(int, input().split())
    c, d = map(int, input().split())
    k1 = a / c
    k2 = b / d
    print(a // max(k1, k2), b // max(k1, k2))


def G():
    n = int(input())
    lst = list(map(float, input().split()))
    while len(lst) > 1:
        for i in range(1, len(lst)):
            lst[i - 1] = abs(lst[i] - lst[i - 1])
        lst.pop()
        print(lst)
    print(abs(lst[0]))


G()