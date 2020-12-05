def f(x):
    return int(x * (x + 1) // 2)


def ans(x):
    l = 1
    r = 1e5
    while r - l > 1:
        mid = int((r + l) // 2)
        if f(mid) > x:
            r = mid
        else:
            l = mid
    # print(x, l, r, f(l), f(r))
    return l if f(l) >= x else r


n = int(input())
while n > 0:
    x = int(input())
    k = ans(x)
    if f(k) != x + 1:
        k += 1
    print(k)
    n -= 1
