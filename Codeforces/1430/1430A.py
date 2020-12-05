t = int(input())


def ans(a):
    if a == 1 or a == 2 or a==4:
        print(-1)
        return
    if a % 3 ==  0:
        print(a // 3, 0, 0)
        return
    if (a - 5) % 3 == 0:
        print((a-5) // 3, 1, 0)
        return
    if (a - 7) % 3 == 0:
        print((a-7) // 3, 0, 1)
        return
    print(-1)


while t:
    t -= 1;
    n = int(input())
    ans(n)
